import datetime
from typing import Dict
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from personne import Personne
from genre import Genre

from vuePersonne import VuePersonne

class VueAnnuaire(QWidget):
    # signal
    nextClicked = pyqtSignal()
    previousClicked = pyqtSignal()
    openFileClicked = pyqtSignal(str)
    newClicked = pyqtSignal()
    personneChanged = pyqtSignal(dict)
    saveAsClicked = pyqtSignal(str)

    # constructor
    def __init__(self):
        super().__init__()

        self.vuePersonne : VuePersonne = VuePersonne()
        self.layout : QVBoxLayout = QVBoxLayout() ; 

        # on va rajouter les boutons
        self.boutonPrecedent : QPushButton = QPushButton("<< précédent")
        self.boutonLoad : QPushButton = QPushButton("load")
        self.boutonNew : QPushButton = QPushButton("new")
        self.boutonSaveas : QPushButton = QPushButton("save as")
        self.boutonSuivant : QPushButton = QPushButton("suivant >>")        

        self.layoutBoutons : QHBoxLayout = QHBoxLayout() 
        self.layoutBoutons.addWidget(self.boutonPrecedent)
        self.layoutBoutons.addWidget(self.boutonLoad)
        self.layoutBoutons.addWidget(self.boutonSaveas)
        self.layoutBoutons.addWidget(self.boutonSuivant)

        # on met le layout de la vue personne
        self.layout.addLayout(self.vuePersonne.layout)
        self.layout.addLayout(self.layoutBoutons)

        self.setLayout(self.layout)
        self.show()

        self.boutonPrecedent.clicked.connect(self.precedent)
        self.boutonLoad.clicked.connect(self.load)
        self.boutonNew.clicked.connect(self.new)
        self.boutonSaveas.clicked.connect(self.saveAs)
        self.boutonSuivant.clicked.connect(self.suivant)

        self.vuePersonne.personneChanged.connect(self.personneModifie)

    def personneModifie(self, dictPersonne: Dict) -> None:
        self.personneChanged.emit(dictPersonne)

    def precedent(self) -> None:
        self.previousClicked.emit()

    def load(self) -> None:
        self.openFileClicked.emit('C:\\Users\\lucie\\OneDrive\\Documents\\Document IUT 1\\R2.02 Dév d\'application avec IHM\\annuaire2\\anphi.json')
        
    def new(self) -> None:
        self.newClicked.emit()

    def saveAs(self) -> None:
        self.saveAsClicked.emit('C:\\Users\\lucie\\OneDrive\\Documents\\Document IUT 1\\R2.02 Dév d\'application avec IHM\\annuaire2\\anphi.json')
        
    def suivant(self) -> None:
        self.nextClicked.emit()

    def updatePersonne(self, personne: Personne):
        self.vuePersonne.updatePersonne(personne.prenom, personne.nom, personne.genre, personne.naissance, personne.mort, personne.bio)

if __name__ == "__main__" :
    import sys
    from PyQt6.QtWidgets import QApplication
    print('TEST: class VueAnnuaire')
    
    app : QApplication = QApplication(sys.argv)
    vueAnnuaire : VueAnnuaire = VueAnnuaire()
    personne : Personne = Personne('Pierre Louis', 'Moreau de Maupertuis', Genre.M, datetime.date(1698, 9, 28), datetime.date(1759, 7, 26), '...')
    vueAnnuaire.updatePersonne(personne)
    
    sys.exit(app.exec())
