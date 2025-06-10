from itertools import combinations
# Exemple du premier graphe

sommet = [1,2,3]
arretes = [(1,2),(1,3),(2,3)]

def transformation(sommet):
    attribut =[]
    clause=[]
    for a in range (len(sommet)):
        clause.append([])
        for b in range (len(sommet)):
            valeur = 3*a+b+1
            attribut.append(valeur)
            clause[a].append(valeur)


    return clause


def creer_clause(sommet):
    clause = transformation(sommet)

    clause2=[]
    for phrase in clause:
        phrase = [x * (-1) for x in phrase ]
        for c in combinations(phrase,2):
            clause2.append(list(c))

    return clause+clause2
        
       

def ajouter_arrete(arretes,nbcouleur):
    clause2=[]
    valeur = 0
    for tup in arretes:
        a,b=tup 
        for indice in range (nbcouleur):
            clause2.append([])
            clause2[valeur].append(-((a-1)*3+(indice+1))) # indice+1 correspond à la couleur
            clause2[valeur].append(-((b-1)*3+(indice+1)))
            valeur +=1
        

    return clause2


clause = creer_clause(sommet) + ajouter_arrete(arretes,3)
print(clause)