def division(a,b):
    if (b !=0):
        return a/b
    else:
        return "division par zero impossible"
    
if __name__=='__main__':
    try:
        a= int(input(" Entrez un nombre a \n"))
        b= int(input(" Entrez un nombre b \n"))
        print("Le resultat de la division est: ", division(a,b))
    
    except ValueError as ex:
        print(ex.__doc__)
        
        
    except ArithmeticError as ex:
        print(ex.__doc__)
        
    except Exception as ex:
        pass
        
    finally:
        print ("sortie par le finally")
    
