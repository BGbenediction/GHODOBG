nombreA=int(input("entrez le nombreA"))
nombreB=int(input("entrez le nombreB"))
symbole=input("entrez un symbole")
resultat=nombreA+nombreB
match symbole:
    case "+":
        resultat=nombreA+nombreB
        print(resultat)
    case "-":
        resultat=nombreA-nombreB
        print(resultat)
    case "*":
        resultat=nombreA*nombreB
        print(resultat)
    case "/":
        resultat=nombreA/nombreB
        print(resultat)
    case _:
        print("symbole non reconnue")

