# main.py — VERSION 100% FONCTIONNELLE AVEC TON VRAI biblio.ui (QListView)

import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from biblio_ui import Ui_Form

# Importe tes contrôleurs
from controller.livres_controller import LivresController
from controller.categorie_controller import CategoriesController
from controller.membre_controller import MembresController
from controller.emprunt_controller import EmpruntsController
from connexion_base import ConnexionBase


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # === STYLE BEAU ===
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50; /* Gris-bleu foncé */
                color: #ecf0f1; /* Blanc cassé */
                font-family: "Segoe UI";
            }
            QLabel#label_2 { 
                font-size: 24pt;
                font-weight: bold;
                color: white;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #8e44ad, stop:1 #3498db); /* Dégradé violet à bleu */
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton {
                background-color: #3498db; /* Bleu */
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #2980b9; /* Bleu plus foncé */
            }
            QTableView {
                background-color: #34495e; /* Gris-bleu plus clair */
                border: 1px solid #2c3e50;
                border-radius: 8px;
                font-size: 10pt;
                selection-background-color: #3498db; /* Bleu pour la sélection */
            }
            QHeaderView::section {
                background-color: #2c3e50;
                color: #ecf0f1;
                padding: 8px;
                border: 1px solid #34495e;
                font-weight: bold;
            }
            QPushButton#pushButton_3 { /* Ajouter */
                background-color: #27ae60; /* Vert */
            }
            QPushButton#pushButton_3:hover {
                background-color: #229954;
            }
            QPushButton#pushButton_5 { /* Modifier */
                background-color: #f39c12; /* Orange */
            }
            QPushButton#pushButton_5:hover {
                background-color: #d35400;
            }
            QPushButton#pushButton_4 { /* Supprimer */
                background-color: #e74c3c; /* Rouge */
            }
            QPushButton#pushButton_4:hover {
                background-color: #c0392b;
            }
        """)

        self.setWindowTitle("BIBLIO-TECH - Gestion de Bibliothèque")

        self.table_view = self.ui.tableView
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Rendre le tableau responsive
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # === Contrôleurs ===
        self.livres_ctrl = LivresController(self.table_view, self)
        self.categories_ctrl = CategoriesController(self.table_view, self)
        self.membres_ctrl = MembresController(self.table_view, self)
        self.emprunts_ctrl = EmpruntsController(self.table_view, self)

        # === Connexions ===
        self.ui.pushButton_2.clicked.connect(self.ouvrir_livres)
        self.ui.pushButton.clicked.connect(self.ouvrir_categories)
        self.ui.emprunt_2.clicked.connect(self.ouvrir_membres)
        self.ui.emprunt.clicked.connect(self.ouvrir_emprunts)

        self.ui.pushButton_3.clicked.connect(self.ajouter)
        self.ui.pushButton_5.clicked.connect(self.modifier)
        self.ui.pushButton_4.clicked.connect(self.supprimer)

        # Page par défaut
        self.current_ctrl = None
        self.ouvrir_livres()

    def ouvrir_livres(self):
        self.current_ctrl = self.livres_ctrl
        self.livres_ctrl.charger()
        self.maj_boutons("Ajouter Livre", "Modifier Livre", "Supprimer Livre")

    def ouvrir_categories(self):
        self.current_ctrl = self.categories_ctrl
        self.categories_ctrl.charger()
        self.maj_boutons("Ajouter Catégorie", "Modifier Catégorie", "Supprimer Catégorie")

    def ouvrir_membres(self):
        self.current_ctrl = self.membres_ctrl
        self.membres_ctrl.charger()
        self.maj_boutons("Ajouter Membre", "Modifier Membre", "Supprimer Membre")

    def ouvrir_emprunts(self):
        self.current_ctrl = self.emprunts_ctrl
        self.emprunts_ctrl.charger()
        self.maj_boutons("Nouvel emprunt", "Retourner livre", "Supprimer emprunt")

    def maj_boutons(self, a, m, s):
        self.ui.pushButton_3.setText(a)
        self.ui.pushButton_5.setText(m)
        self.ui.pushButton_4.setText(s)

    def ajouter(self):
        if self.current_ctrl:
            self.current_ctrl.ajouter()

    def modifier(self):
        if self.current_ctrl:
            if self.current_ctrl == self.emprunts_ctrl:
                self.emprunts_ctrl.retourner_livre()
            else:
                self.current_ctrl.modifier()

    def supprimer(self):
        if self.current_ctrl:
            self.current_ctrl.supprimer()


if __name__ == "__main__":
    ConnexionBase.initialisation_bd()
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.resize(900, 700)
    window.show()
    sys.exit(app.exec())