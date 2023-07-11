min_intervalle = int(input("entrez une valeur minimale d'un intervalle"))
max_intervalle = int(input("entrez une valeur maximale d'un intervalle"))
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

for i in range(min_intervalle,max_intervalle):
    if (is_prime(i)):
        print (i)
        
