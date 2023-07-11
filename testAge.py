age= int(input("Entrez votre age"))
if ( age>=0 and age<17):
    print("vous avez ",age,"ans\nVous etes mineur")
elif ( age<50):
     print("vous avez ",age,"ans\nVous etes majeur")
elif ( age<=100):
     print("vous avez ",age,"ans\nVous etes senior")
elif ( age>100):
    print("vous avez ",age,"ans\nVous tres agé ")
else :
    print("Vous avez saisi un mauvais age")
