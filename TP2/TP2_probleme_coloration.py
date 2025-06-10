from itertools import combinations
import subprocess

# Exemple du premier graphe

sommet1 = [1,2,3]
arretes1 = [(1,2),(1,3),(2,3)]

sommet2 = [ 1,2,3,4,5,6,7,8,9,10]
arretes2 = [(1,2),(1,3),(1,6),(2,4),(2,7),(4,5),(4,9),(5,3),(5,10),(3,8),(6,9),(9,8),(7,8),(7,10),(6,10)]

def transformation(sommet):
    attribut =[]
    clause=[]
    for a in range (len(sommet)):
        clause.append([])
        for b in range (3):
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


def inserer_fichier(clause,sommet1,nbcouleur,filename):
    with open(filename, "w") as f:
        f.write("c Exemple de coloration de graphe simple\n")
        f.write(f"p cnf {len(sommet1)*nbcouleur} {len(clause)}\n")
        for phrase in clause:
            for element in phrase:
                f.write(str(element)+ " ")
            f.write(" 0\n")



def exec_gophersat(
    filename: str, cmd: str = "gophersat", encoding: str = "utf8") -> tuple[bool, list[int]]:
    result = subprocess.run(
        [cmd, filename], capture_output=True, check=True, encoding=encoding
    )
    string = str(result.stdout)
    lines = string.splitlines()

    if lines[1] != "s SATISFIABLE":
        return False, []

    model = lines[2][2:-2].split(" ")

    return True, [int(x) for x in model]


# fonction principale
def solveur(sommet : list[int], arretes: list[tuple[int,int]], nbcouleurs : int, filename : str) -> str:
    clause = creer_clause(sommet) + ajouter_arrete(arretes,nbcouleurs)
    #on génère le fichier
    inserer_fichier(clause,sommet,nbcouleurs,filename)
    # on l'exécute
    solution =exec_gophersat(filename)
    if solution[0]:
        print("SAT !")
        affichage(solution[1],["R","V","B"])
    else:
        print("UNSAT!")

#gere l'affichage
def affichage(clauses : list[int], couleurs : list[str]) -> str:
    sommet = 1
    for i in range (len(clauses)):
        if clauses[i] > 0:
            # On souhaite l'afficher
            print(f"sommet {sommet} = {couleurs[i%len(couleurs)]}")
            sommet +=1


#clause = creer_clause(sommet2) + ajouter_arrete(arretes2,3)
#inserer_fichier(clause,sommet2,3,"test.cnf")
#print(exec_gophersat("coloration_graphe_complique.cnf"))

# Exemple du deuxième graphe
solveur(sommet1,arretes1,3,"coloration.cnf")