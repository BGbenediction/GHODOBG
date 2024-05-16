class Forme:
    def __init__(self,largeur,longueur):
        self.largeur=largeur
        self.longeur=longueur

class Triangle(Forme):
    def Aire(self):
        return(self.largeur*self.longeur)/2
    
class Rectangle(Forme):
    def Aire(self):
        return self.largeur*self.longeur
rectangle=Rectangle(100,200)
triangle=Triangle(100,150)
print(rectangle.Aire())
print(triangle.Aire())