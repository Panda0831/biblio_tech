# controleur/livres_controller.py

from PySide6.QtWidgets import (
    QMessageBox, QInputDialog, QLineEdit
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from modele.livres_modele import LivresModel
from modele.categories_modele import CategoriesModel
from modele.emprun_modele import EmpruntModele


class LivresController:
    def __init__(self, table_view, parent_window):
        self.table = table_view
        self.parent = parent_window

    def charger(self):
        """Charge tous les livres avec le NOM de la catégorie (pas l'ID !)"""
        livres = LivresModel.get_all_livres()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Titre", "Catégorie"])

        for livre in livres:
            livre_id, titre, cat_id = livre
            
            cat = CategoriesModel.get_categorie_by_id(cat_id)
            nom_categorie = cat[1] if cat else "Catégorie supprimée"

            items = [
                QStandardItem(str(livre_id)),
                QStandardItem(titre),
                QStandardItem(nom_categorie)
            ]
            items[0].setEditable(False)
            model.appendRow(items)

        self.table.setModel(model)

    def ajouter(self):
        """Ajouter un nouveau livre"""
        titre, ok1 = QInputDialog.getText(
            self.parent, "Nouveau livre", "Titre du livre :", QLineEdit.Normal
        )
        if not ok1 or not titre.strip():
            if ok1:
                QMessageBox.warning(self.parent, "Attention", "Le titre est obligatoire !")
            return

        cat_id, ok2 = QInputDialog.getInt(
            self.parent, "Catégorie", "ID de la catégorie :"
        )
        if not ok2:
            return

        if not CategoriesModel.get_categorie_by_id(cat_id):
            QMessageBox.critical(self.parent, "Erreur", f"La catégorie ID {cat_id} n'existe pas !")
            return

        try:
            LivresModel.ajouter_livre(titre.strip(), cat_id)
            QMessageBox.information(self.parent, "Succès", "Livre ajouté avec succès !")
            self.charger()
        except Exception as e:
            QMessageBox.critical(self.parent, "Erreur", f"Impossible d'ajouter :\n{str(e)}")

    def modifier(self):
        """Modifier le livre sélectionné"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Sélectionnez un livre à modifier !")
            return

        row = selected[0].row()
        livre_id = int(self.table.model().item(row, 0).text())
        ancien_titre = self.table.model().item(row, 1).text()

        livre = LivresModel.get_livre_by_id(livre_id)
        if not livre:
            QMessageBox.critical(self.parent, "Erreur", "Livre introuvable en base !")
            return
        ancien_cat_id = livre[2]

        nouveau_titre, ok1 = QInputDialog.getText(
            self.parent, "Modifier livre", "Nouveau titre :", QLineEdit.Normal, ancien_titre
        )
        if not ok1:
            return
        if not nouveau_titre.strip():
            QMessageBox.warning(self.parent, "Erreur", "Le titre ne peut pas être vide !")
            return

        nouveau_cat_id, ok2 = QInputDialog.getInt(
            self.parent, "Catégorie", "Nouvel ID catégorie :", defaultValue=ancien_cat_id
        )
        if not ok2:
            return

        if not CategoriesModel.get_categorie_by_id(nouveau_cat_id):
            QMessageBox.critical(self.parent, "Erreur", f"La catégorie ID {nouveau_cat_id} n'existe pas !")
            return

        LivresModel.modifier_livre(livre_id, nouveau_titre.strip(), nouveau_cat_id)
        QMessageBox.information(self.parent, "Modifié", "Livre mis à jour !")
        self.charger()

    def supprimer(self):
        """Supprimer le livre sélectionné"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Sélectionnez un livre à supprimer !")
            return

        row = selected[0].row()
        livre_id = int(self.table.model().item(row, 0).text())
        titre = self.table.model().item(row, 1).text()

        # Vérification des emprunts en cours
        emprunts = EmpruntModele.get_emprunts_by_livre(livre_id)
        emprunts_en_cours = [e for e in emprunts if e[5] is None]
        if emprunts_en_cours:
            QMessageBox.critical(
                self.parent,
                "Suppression impossible",
                f"Le livre « {titre} » est actuellement emprunté.\n"
                "Demandez le retour du livre avant de le supprimer."
            )
            return

        reponse = QMessageBox.question(
            self.parent,
            "Confirmer suppression",
            f"Voulez-vous vraiment supprimer le livre :\n\n« {titre} » (ID: {livre_id}) ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reponse == QMessageBox.Yes:
            try:
                LivresModel.supprimer_livre(livre_id)
                QMessageBox.information(self.parent, "Supprimé", "Livre supprimé avec succès !")
                self.charger()
            except Exception as e:
                QMessageBox.critical(self.parent, "Erreur", f"Impossible de supprimer :\n{str(e)}")