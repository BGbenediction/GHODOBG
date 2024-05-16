class Account:
    def __init__(self,soldeInitial=0):
        self.soldeInitial=soldeInitial
        self.soldeActuel=self.soldeInitial
    def get_balance(self):
        return self.soldeActuel
    def deponser(self,montant):
        self.soldeActuel=self.soldeActuel+montant
    def retirer(self,montant):
        self.soldeActuel=self.soldeActuel-montant
    def ajouterInteret(self,taux):
        self.soldeActuel=self.soldeActuel*(1+taux)


niveauCompte=Account()
niveauCompte.deponser(60)
niveauCompte.retirer(20)
niveauCompte.ajouterInteret(2)
print(niveauCompte.get_balance())