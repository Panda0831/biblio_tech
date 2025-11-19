# controleur/emprunts_controller.py

from PySide6.QtWidgets import (
    QMessageBox, QInputDialog, QLineEdit, QDateEdit
)
from PySide6.QtCore import QDate
from PySide6.QtGui import QStandardItemModel, QStandardItem

from modele.emprun_modele import EmpruntModele


class EmpruntsController:
    def __init__(self, table_view, parent_window):
        self.table = table_view
        self.parent = parent_window

    def charger(self):
        """Charge tous les emprunts dans le tableau"""
        emprunts = EmpruntModele.get_all_emprunts()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "ID", "ID Livre", "ID Membre", "Date Emprunt", "Date Prévue", "Date Retour", "Statut"
        ])

        for emp in emprunts:
            statut = "Retourné" if emp[5] else "En cours"
            items = [
                QStandardItem(str(emp[0])),           # ID
                QStandardItem(str(emp[1])),           # ID Livre
                QStandardItem(str(emp[2])),           # ID Membre
                QStandardItem(emp[3] or "-"),         # Date emprunt
                QStandardItem(emp[4] or "-"),         # Date prévue
                QStandardItem(emp[5] or "Non retourné"),  # Date retour
                QStandardItem(statut)
            ]
            # Colonne ID non éditable
            items[0].setEditable(False)
            model.appendRow(items)

        self.table.setModel(model)

    def ajouter(self):
        """Enregistrer un nouvel emprunt"""
        id_livre, ok1 = QInputDialog.getInt(self.parent, "Nouvel emprunt", "ID du livre :")
        if not ok1: return

        id_membre, ok2 = QInputDialog.getInt(self.parent, "Nouvel emprunt", "ID du membre :")
        if not ok2: return

        date_emprunt, ok3 = QInputDialog.getText(
            self.parent, "Date", "Date d'emprunt (AAAA-MM-JJ) :", text=QDate.currentDate().toString("yyyy-MM-dd")
        )
        if not ok3: return

        date_prevue, ok4 = QInputDialog.getText(
            self.parent, "Date", "Date de retour prévue (AAAA-MM-JJ) :"
        )
        if not ok4: return

        try:
            EmpruntModele.enregistrer_emprunt(id_livre, id_membre, date_emprunt, date_prevue)
            QMessageBox.information(self.parent, "Succès", "Emprunt enregistré avec succès !")
            self.charger()
        except Exception as e:
            QMessageBox.critical(self.parent, "Erreur", f"Impossible d'enregistrer :\n{str(e)}")

    def retourner_livre(self):
        """Marquer un livre comme retourné"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Sélectionnez un emprunt à retourner !")
            return

        row = selected[0].row()
        emp_id = int(self.table.model().item(row, 0).text())
        date_retour_actuelle = self.table.model().item(row, 5).text()

        if date_retour_actuelle != "Non retourné":
            QMessageBox.information(self.parent, "Info", "Ce livre a déjà été retourné.")
            return

        date_retour, ok = QInputDialog.getText(
            self.parent,
            "Retour de livre",
            "Date de retour réelle (AAAA-MM-JJ) :",
            text=QDate.currentDate().toString("yyyy-MM-dd")
        )
        if not ok: return

        try:
            EmpruntModele.retourner_livre(emp_id, date_retour)
            QMessageBox.information(self.parent, "Retour enregistré", "Livre retourné avec succès !")
            self.charger()
        except Exception as e:
            QMessageBox.critical(self.parent, "Erreur", str(e))

    def supprimer(self):
        """Supprimer un emprunt (admin seulement)"""
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self.parent, "Attention", "Sélectionnez un emprunt à supprimer !")
            return

        row = selected[0].row()
        emp_id = int(self.table.model().item(row, 0).text())
        livre_id = self.table.model().item(row, 1).text()
        membre_id = self.table.model().item(row, 2).text()

        reponse = QMessageBox.question(
            self.parent,
            "Confirmer suppression",
            f"Supprimer l'emprunt ID {emp_id} ?\n"
            f"Livre ID: {livre_id} | Membre ID: {membre_id}\n\n"
            "Cette action est irréversible !",
            QMessageBox.Yes | QMessageBox.No
        )
        if reponse == QMessageBox.Yes:
            EmpruntModele.supprimer_emprunt(emp_id)  # corrigé : suppirimer → supprimer
            QMessageBox.information(self.parent, "Supprimé", "Emprunt supprimé.")
            self.charger()

    # Option bonus : afficher un seul emprunt (pas obligatoire)
    def afficher_un_emprunt(self):
        emp_id, ok = QInputDialog.getInt(self.parent, "Rechercher", "ID de l'emprunt :")
        if not ok: return
        emprunt = EmpruntModele.get_emprunt_by_id(emp_id)
        if emprunt:
            statut = "Retourné" if emprunt[5] else "En cours"
            msg = f"""
            <b>Emprunt ID :</b> {emprunt[0]}<br>
            <b>Livre ID :</b> {emprunt[1]}<br>
            <b>Membre ID :</b> {emprunt[2]}<br>
            <b>Date emprunt :</b> {emprunt[3]}<br>
            <b>Date prévue :</b> {emprunt[4]}<br>
            <b>Date retour :</b> {emprunt[5] or "Non retourné"}<br>
            <b>Statut :</b> {statut}
            """
            QMessageBox.information(self.parent, "Détail emprunt", msg)
        else:
            QMessageBox.warning(self.parent, "Non trouvé", "Aucun emprunt avec cet ID.")