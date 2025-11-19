# controleur/categories_controller.py

from PySide6.QtWidgets import (
    QMessageBox, QInputDialog, QLineEdit
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from modele.categories_modele import CategoriesModel
from modele.livres_modele import LivresModel


class CategoriesController:
    def __init__(self, table_view, parent_window):
        """
        table_view : ton QTableView (self.ui.tableView)
        parent_window : la fenêtre principale (self)
        """
        self.table = table_view
        self.parent = parent_window

    def charger(self):
        """Charge toutes les catégories dans le QTableView"""
        categories = CategoriesModel.get_all_categories()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Nom de la catégorie"])

        for cat in categories:
            id_item = QStandardItem(str(cat[0]))
            nom_item = QStandardItem(cat[1])
            # Rend l'ID non éditable directement (optionnel)
            id_item.setEditable(False)
            model.appendRow([id_item, nom_item])

        self.table.setModel(model)

    def ajouter(self):
        """Ajouter une nouvelle catégorie"""
        nom, ok = QInputDialog.getText(
            self.parent,
            "Nouvelle catégorie",
            "Entrez le nom de la catégorie :",
            QLineEdit.Normal
        )
        if ok and nom.strip():
            CategoriesModel.ajouter_categorie(nom.strip())
            QMessageBox.information(self.parent, "Succès", "Catégorie ajoutée avec succès !")
            self.charger()
        elif ok:
            QMessageBox.warning(self.parent, "Attention", "Le nom ne peut pas être vide !")

    def modifier(self):
        """Modifier la catégorie sélectionnée"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Veuillez sélectionner une catégorie à modifier.")
            return

        row = selected[0].row()
        cat_id = int(self.table.model().item(row, 0).text())
        ancien_nom = self.table.model().item(row, 1).text()

        nouveau_nom, ok = QInputDialog.getText(
            self.parent,
            "Modifier la catégorie",
            "Nouveau nom :",
            QLineEdit.Normal,
            ancien_nom
        )

        if not ok:
            return
        if not nouveau_nom.strip():
            QMessageBox.warning(self.parent, "Erreur", "Le nom ne peut pas être vide !")
            return
        if nouveau_nom.strip() == ancien_nom:
            return  # rien à faire

        CategoriesModel.modifier_categorie(cat_id, nouveau_nom.strip())
        QMessageBox.information(self.parent, "Modifié", "Catégorie mise à jour !")
        self.charger()

    def supprimer(self):
        """Supprimer la catégorie sélectionnée (avec protection)"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Veuillez sélectionner une catégorie à supprimer.")
            return

        row = selected[0].row()
        cat_id = int(self.table.model().item(row, 0).text())
        cat_nom = self.table.model().item(row, 1).text()

        # Protection : y a-t-il des livres associés ?
        livres = LivresModel.get_livres_by_categorie(cat_id)
        if livres:
            QMessageBox.critical(
                self.parent,
                "Suppression impossible",
                f"La catégorie « {cat_nom} » contient {len(livres)} livre(s).\n"
                "Supprimez ou déplacez ces livres avant."
            )
            return

        # Confirmation
        reponse = QMessageBox.question(
            self.parent,
            "Confirmer la suppression",
            f"Voulez-vous vraiment supprimer la catégorie :\n\n« {cat_nom} » ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reponse == QMessageBox.Yes:
            CategoriesModel.supprimer_categorie(cat_id)
            QMessageBox.information(self.parent, "Supprimé", "Catégorie supprimée avec succès !")
            self.charger()