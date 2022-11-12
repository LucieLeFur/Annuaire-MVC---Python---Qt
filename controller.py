from personne import Personne
from annuaire import Annuaire
from genre import Genre
from vueAnnuaire import VueAnnuaire
import datetime
from typing import Union

class Controller:
    # constructor
    def __init__(self) -> None:
        # attrbut
        self.modele = Annuaire('C:\\Users\\lucie\\OneDrive\\Documents\\Document IUT 1\\R2.02 Dév d\'application avec IHM\\annuaire2\\anphi.json')
        self.vue = VueAnnuaire()
        p = self.modele.getPersonne() 
        if isinstance(p, Personne):
            self.vue.updatePersonne(p)
        
        # slots ie callback
        self.vue.nextClicked.connect(self.next)
        self.vue.previousClicked.connect(self.previous)
        self.vue.openFileClicked.connect(self.openFile)
        self.vue.newClicked.connect(self.new)
        self.vue.personneChanged.connect(self.update)
        self.vue.saveAsClicked.connect(self.saveAs)
 
    def update(self,d) -> None:
        personne = Personne(d["prenom"], d["nom"], d["genre"],  d["naissance"], d["mort"], d["bio"]) 
        self.modele.update(personne)
 
    def next(self) -> None:
        self.modele.next()
        p: Union[Personne, None] = self.modele.getPersonne()
        if (p):
            self.vue.updatePersonne(p)

    def previous(self) -> None:
        self.modele.previous()
        p: Union[Personne, None] = self.modele.getPersonne()
        if (p):       
            self.vue.updatePersonne(p)
 
    def new(self) -> None:
        personne: Personne = Personne(' ', ' ', Genre.M, datetime.date(1, 1, 1), None, '')
        self.modele.addPersonne(personne)
        p: Union[Personne, None] = self.modele.getPersonne()
        if (p): 
            self.vue.updatePersonne(personne)

    def openFile(self, fname : str) -> None:
        self.modele.open(fname)  
        p: Union[Personne, None] = self.modele.getPersonne()
        if (p):              
            self.vue.updatePersonne(p)

    def saveAs(self, fname: str) -> None:
        self.modele.save(fname)
        print("saveAs")

if __name__ == "__main__" :
    import sys
    from PyQt6.QtWidgets import QApplication
    print('TEST: class Controller')
    
    app : QApplication = QApplication(sys.argv)
    controller : Controller = Controller()
 
    
    sys.exit(app.exec())