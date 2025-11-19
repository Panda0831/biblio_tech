# controleur/membres_controller.py

from PySide6.QtWidgets import (
    QMessageBox, QInputDialog, QLineEdit
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from modele.membres_modele import MembreModele
from modele.emprun_modele import EmpruntModele  # pour vérifier les emprunts en cours


class MembresController:
    def __init__(self, table_view, parent_window):
        self.table = table_view
        self.parent = parent_window
    def charger(self):
        membres = MembreModele.get_all_membre()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Nom complet", "Contact", "Statut"])

        for membre in membres:
            mem_id, nom, contact = membre[0], membre[1], membre[2]

            # Compte les emprunts NON RETOURNÉS (date_retour is None)
            emprunts_en_cours = [
                e for e in EmpruntModele.get_all_emprunts()
                if e[2] == mem_id and e[5] is None
            ]
            statut = f"{len(emprunts_en_cours)} emprunt(s) en cours" if emprunts_en_cours else "Libre"

            model.appendRow([
                QStandardItem(str(mem_id)),
                QStandardItem(nom),
                QStandardItem(contact),
                QStandardItem(statut)
            ])

        self.table.setModel(model)

    def ajouter(self):
        """Ajouter un nouveau membre"""
        nom, ok1 = QInputDialog.getText(
            self.parent, "Nouveau membre", "Nom complet :", QLineEdit.Normal
        )
        if not ok1 or not nom.strip():
            if ok1: QMessageBox.warning(self.parent, "Erreur", "Le nom est obligatoire !")
            return

        contact, ok2 = QInputDialog.getText(
            self.parent, "Contact", "Contact (email/téléphone) :", QLineEdit.Normal
        )
        if not ok2:
            return

        try:
            MembreModele.ajouter_membre(nom.strip(), contact.strip())
            QMessageBox.information(self.parent, "Succès", "Membre ajouté avec succès !")
            self.charger()
        except Exception as e:
            QMessageBox.critical(self.parent, "Erreur", f"Impossible d'ajouter :\n{str(e)}")

    def modifier(self):
        """Modifier le membre sélectionné"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Sélectionnez un membre à modifier !")
            return

        row = selected[0].row()
        mem_id = int(self.table.model().item(row, 0).text())
        ancien_nom = self.table.model().item(row, 1).text()
        ancien_contact = self.table.model().item(row, 2).text()

        nouveau_nom, ok1 = QInputDialog.getText(
            self.parent, "Modifier membre", "Nouveau nom :", QLineEdit.Normal, ancien_nom
        )
        if not ok1: return
        if not nouveau_nom.strip():
            QMessageBox.warning(self.parent, "Erreur", "Le nom ne peut pas être vide !")
            return

        nouveau_contact, ok2 = QInputDialog.getText(
            self.parent, "Modifier membre", "Nouveau contact :", QLineEdit.Normal, ancien_contact
        )
        if not ok2: return

        MembreModele.modifier_membre(mem_id, nouveau_nom.strip(), nouveau_contact.strip())
        QMessageBox.information(self.parent, "Modifié", "Membre mis à jour !")
        self.charger()

    def supprimer(self):
        """Supprimer un membre (seulement s'il n'a pas d'emprunt en cours)"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Sélectionnez un membre à supprimer !")
            return

        row = selected[0].row()
        mem_id = int(self.table.model().item(row, 0).text())
        nom = self.table.model().item(row, 1).text()

        # Vérification des emprunts en cours
        emprunts = EmpruntModele.get_emprunts_en_cours_by_membre(mem_id)
        if emprunts:
            QMessageBox.critical(
                self.parent,
                "Suppression impossible",
                f"Le membre « {nom} » a {len(emprunts)} emprunt(s) en cours.\n"
                "Demandez le retour des livres avant de supprimer."
            )
            return

        reponse = QMessageBox.question(
            self.parent,
            "Confirmer suppression",
            f"Voulez-vous vraiment supprimer le membre :\n\n« {nom} » (ID: {mem_id}) ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reponse == QMessageBox.Yes:
            MembreModele.supprimer_membre(mem_id)
            QMessageBox.information(self.parent, "Supprimé", "Membre supprimé avec succès !")
            self.charger()