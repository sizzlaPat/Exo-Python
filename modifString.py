a =" AnAlaoienr "
b ="123"
print(type(a)) # retourne le type de donnée 'str'
print(len(a))# retourne 12 => nombre decaractères de a

print(a.isupper()) # retourne false
print(a.islower()) # retourne false
print(a.upper())# ANALAOIENR
print(a.isalpha())# retourne False , car a contient ' '
print(b.isnumeric())# true
print(b.isdecimal())# true
print(a[2].isdigit())# false
print(a.istitle())# false => car a ne débute pas par une lettre majuscule
print(a.strip())# AnAlaoienr => enleve l'espace qu'il y a au début et à lafin

print(a.join(b)) # 1 AnAlaoienr 2 AnAlaoienr 3 => assemble a et b
