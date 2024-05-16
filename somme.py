class somme:
    def __init__(self,nombre1,nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
    def som(self,nombre1,nombre2):
        resultat=nombre1 + nombre2
        return resultat
    
nombre_utilisateur1= int(input("Entrez le nombre 1"))
nombre_utilisateur2= int(input("Entrez le nombre 2"))

som1= somme(nombre_utilisateur1,nombre_utilisateur2)
print(f"la somme de {nombre_utilisateur1} et {nombre_utilisateur2}={nombre_utilisateur1,nombre_utilisateur2}")