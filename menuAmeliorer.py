menu=["banane","citron","menthe"]
print ("choix du menu")
for i in range (0,len(menu)):
    print(i+1,")",menu[i],"\n") 
    
choix=int( input("Entrez votre choix : "))

print("Votre choix du menu est :" , menu[choix-1])
