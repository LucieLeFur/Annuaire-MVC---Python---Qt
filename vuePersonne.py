# --- import 
from PyQt6.QtWidgets import QWidget, QLineEdit, QTextEdit,QDateEdit,QComboBox
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, QDate
from genre import Genre
import datetime, genre as g
from typing import Dict, Union

# ----------------------------------------------------
# --- class VuePersonne
# ----------------------------------------------------
class VuePersonne(QWidget):
    # signal
    personneChanged : pyqtSignal = pyqtSignal(dict)
    
    # constructor
    def __init__(self):
        super().__init__()
        self.genre : QComboBox = QComboBox()
        self.genre.addItems(["M. ", "Mme ", "_ "])
        self.prenom : QLineEdit = QLineEdit("Prénom")
        self.nom : QLineEdit = QLineEdit("Nom")

        self.dateNAissanceLabel = QLabel(self)
        self.dateNAissanceLabel.setText('Né le:')
        self.dateNaissance : QDateEdit = QDateEdit()
        self.dateNaissance.setDateRange(QDate(1,1,1),QDate.currentDate())
        
        self.dateMortLabel = QLabel(self)
        self.dateMortLabel.setText('Mort le:')
        self.dateMort : QDateEdit = QDateEdit() 
        self.dateMort.setDateRange(QDate(1,1,1),QDate.currentDate())

        self.bio : QTextEdit = QTextEdit('"biographie"')

        self.layout : QVBoxLayout = QVBoxLayout() ; 
        self.layoutPresentation : QHBoxLayout = QHBoxLayout() ; 
        self.layoutPresentation.addStretch(1)
        self.layoutPresentation.addWidget(self.genre)
        self.layoutPresentation.addWidget(self.prenom)
        self.layoutPresentation.addWidget(self.nom)
        
        self.layoutDates : QHBoxLayout = QHBoxLayout()
        self.layoutDates.addStretch(1)     
        self.layoutDates.addWidget(self.dateNAissanceLabel)      
        self.layoutDates.addWidget(self.dateNaissance)
        self.layoutDates.addWidget(self.dateMortLabel)      
        self.layoutDates.addWidget(self.dateMort)
        self.layoutDates.addStretch(1)  

        self.layout.addLayout(self.layoutPresentation)
        self.layout.addLayout(self.layoutDates)
        self.layout.addWidget(self.bio)      

        self.genre.currentIndexChanged.connect(self.changeGenre)
        self.prenom.editingFinished.connect(self.changePrenom)
        self.nom.editingFinished.connect(self.changeNom)
        self.bio.textChanged.connect(self.changeBiographie)
        self.dateNaissance.dateChanged.connect(self.changeNaissance)
        self.dateMort.dateChanged.connect(self.changeMort)      
        
    # callback
    def modificationPersonne(self) -> None:
        dictPersonne: Dict = {
            'genre'  : Genre(self.genre.currentIndex() + 1),
            'prenom': self.prenom.text(),
            'nom'    : self.nom.text(),
            'naissance' : self.dateNaissance.date().toPyDate(),
            'mort'      : self.dateMort.date().toPyDate(),
            'bio'    : self.bio.toPlainText()
        }      
        self.personneChanged.emit(dictPersonne)        

    def changeGenre(self) -> None:
        self.modificationPersonne()
    
    def changePrenom(self) -> None:
        self.modificationPersonne()

    def changeNom(self) -> None:
        self.modificationPersonne()

    def changeNaissance(self) -> None:
         self.modificationPersonne()     
    
    def changeMort(self) -> None:
         self.modificationPersonne() 
    
    def changeBiographie(self) -> None:
         self.modificationPersonne()          
            
    def getAllInfo(self) -> None:
         self.modificationPersonne()  

    # update : mise à jour de la vue
    def updatePersonne(self, prenom: str, nom: str, genre: g.Genre, nee: datetime.date, mort: (Union[datetime.date,None]),
        bio: str) -> None:
        self.nom.setText(nom)
        self.prenom.setText(prenom)
        self.genre.setCurrentIndex(genre.value - 1)
        self.dateNaissance.setDate(nee)
        if (mort == None):
            self.dateMort.setDate(datetime.date(1, 1, 1))
        else:
            self.dateMort.setDate(mort)

        self.bio.setText(bio)
        print("updatePersonne")    
        
if __name__ == "__main__" :
    import sys
    from PyQt6.QtWidgets import QApplication
    print('TEST: class VuePersonne')

    app : QApplication = QApplication(sys.argv)
    vuePersonne : VuePersonne = VuePersonne()
    vuePersonne.updatePersonne('Pierre Louis', 'Moreau de Maupertuis', Genre.M, datetime.date(1698, 9, 28), datetime.date(1759, 7, 26), '...')
    vuePersonne.setLayout(vuePersonne.layout) 
    vuePersonne.show()
    
    sys.exit(app.exec())



