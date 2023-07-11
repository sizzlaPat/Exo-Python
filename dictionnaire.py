
items_employee=["Nom","Prenom","Age","Salaire","role"]
employee_List=[]

start=True
while(start):
    Employee= {}
    for i in range (0,len(items_employee)):
        
        print("Remplir le champ ", items_employee[i])
        Employee[items_employee[i]]= input("merci de saisir une valeur\n")
    employee_List.append(Employee)

    reponse= input("voulez vous sasisir un nouvelle employée? O/N \n")
    if( reponse == "N" or reponse == "n"):
        start=False
for i in range (0,len(employee_List)):
    for x,y in employee_List[i].items():
        print(x,y)
    




    

