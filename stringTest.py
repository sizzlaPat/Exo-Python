def salut(texte):
    texte=f""" Salut mon ami {texte} ! / Yoyeux anniversaire {texte}! """
    return (texte)
def division(a,b):
    if (b !=0):
        return a/b
    else:
        return "division par zero impossible"
    
if __name__=='__main__':
    text = salut("toto")
    print(text)
    nom= salut(input("Merci de saisir un nom \n"))
    print(nom)
    a= int(input(" Entrez un nombre a \n"))
    b= int(input(" Entrez un nombre b \n"))
    print("Le resultat de la division est: ", division(a,b))
             
