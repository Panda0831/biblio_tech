# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'biblio.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QLabel, QTableView,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(755, 680)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalWidget = QWidget(Form)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setStyleSheet(u"background-color: #3C3C3C; border-radius: 10px;")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.emprunt_2 = QPushButton(self.horizontalWidget)
        self.emprunt_2.setObjectName(u"emprunt_2")
        self.emprunt_2.setStyleSheet(u"background-color: #007BFF; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.emprunt_2)

        self.pushButton_2 = QPushButton(self.horizontalWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: #007BFF; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.emprunt = QPushButton(self.horizontalWidget)
        self.emprunt.setObjectName(u"emprunt")
        self.emprunt.setStyleSheet(u"background-color: #007BFF; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.emprunt)

        self.pushButton = QPushButton(self.horizontalWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: #007BFF; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.pushButton)
        # Header label
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: #2E2E2E; border-radius: 10px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMaximumHeight(60)

        # Add the horizontal button bar and header to the main vertical layout
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.horizontalWidget)

        # Central area: table on the left, action buttons on the right
        self.centralWidget = QWidget(Form)
        self.centralLayout = QHBoxLayout(self.centralWidget)
        self.centralLayout.setObjectName(u"centralLayout")

        self.tableView = QTableView(self.centralWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: #3C3C3C; border-radius: 16px; color: white;")
        self.tableView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.centralLayout.addWidget(self.tableView)

        # Right-side vertical group for action buttons
        self.rightWidget = QWidget(self.centralWidget)
        self.rightLayout = QVBoxLayout(self.rightWidget)
        self.rightLayout.setObjectName(u"rightLayout")

        self.pushButton_3 = QPushButton(self.rightWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: #28a745; color: white; border-radius: 16px; padding: 10px 24px; font-weight: bold;")

        self.pushButton_5 = QPushButton(self.rightWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: #007BFF; color: white; border-radius: 16px; padding: 10px 24px; font-weight: bold;")

        self.pushButton_4 = QPushButton(self.rightWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: #dc3545; color: white; border-radius: 16px; padding: 8px 16px; font-weight: bold;")

        self.rightLayout.addWidget(self.pushButton_3)
        self.rightLayout.addWidget(self.pushButton_5)
        self.rightLayout.addWidget(self.pushButton_4)
        self.rightLayout.addStretch(1)

        self.centralLayout.addWidget(self.rightWidget)
        self.verticalLayout.addWidget(self.centralWidget)
        QWidget.setTabOrder(self.emprunt_2, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.emprunt)
        QWidget.setTabOrder(self.emprunt, self.pushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.emprunt_2.setText(QCoreApplication.translate("Form", u"membres", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"livres", None))
        self.emprunt.setText(QCoreApplication.translate("Form", u"emprunt", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"categorie", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"BIBLIO-TECH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"suppimer", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"ajouter", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"modifier", None))
    # retranslateUi

