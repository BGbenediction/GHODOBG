class rectangle:
    largeur=3
    hauteur=2
#METHODES
    def class_surface(self):
        return self.largeur*self.hauteur
    #INSTATION DE CLASS OU OBJET
rectangle1=rectangle()
print(f" rectangle1 a pour  hauteur de:{rectangle1.hauteur}")

rectangle2=rectangle()
print(f" rectangle2 a pour largeur de: {rectangle2.largeur}")