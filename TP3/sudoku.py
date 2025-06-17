

from typing import List, Tuple
from pprint import pprint
from itertools import combinations
import subprocess
from math import sqrt

# alias de types
Grid = List[List[int]] 
PropositionnalVariable = int
Literal = int
Clause = List[Literal]
ClauseBase = List[Clause]
Model = List[Literal]

model = [-1, -2, -3, -4, 5, -6, -7, -8, -9, -10, -11, 12, -13, -14, -15, -16, -17, -18, -19, -20, -21, 22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, 33, -34, -35, -36, -37, -38, -39, -40, -41, -42, 43, -44, -45, -46, -47, -48, -49, -50, -51, -52, 53, -54, -55, -56, -57, -58, -59, -60, -61, -62, 63, 64, -65, -66, -67, -68, -69, -70, -71, -72, -73, 74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, 87, -88, -89, -90, -91, -92, -93, -94, -95, -96, 97, -98, -99, -100, 101, -102, -103, -104, -105, -106, -107, -108, 109, -110, -111, -112, -113, -114, -115, -116, -117, -118, -119, -120, -121, -122, -123, -124, -125, 126, -127, -128, -129, -130, 131, -132, -133, -134, -135, -136, -137, 138, -139, -140, -141, -142, -143, -144, -145, -146, -147, 148, -149, -150, -151, -152, -153, -154, -155, -156, -157, -158, -159, -160, 161, -162, 163, -164, -165, -166, -167, -168, -169, -170, -171, -172, -173, -174, -175, -176, -177, -178, -179, 180, -181, -182, -183, -184, -185, -186, -187, 188, -189, -190, -191, 192, -193, -194, -195, -196, -197, -198, -199, -200, -201, 202, -203, -204, -205, -206, -207, -208, 209, -210, -211, -212, -213, -214, -215, -216, -217, -218, -219, -220, 221, -222, -223, -224, -225, -226, -227, -228, -229, -230, 231, -232, -233, -234, -235, -236, -237, -238, -239, -240, 241, -242, -243, -244, -245, -246, -247, -248, -249, -250, 251, -252, -253, -254, -255, -256, 257, -258, -259, -260, -261, -262, -263, -264, -265, -266, -267, -268, -269, 270, -271, -272, -273, -274, -275, -276, 277, -278, -279, -280, -281, -282, -283, -284, 285, -286, -287, -288, 289, -290, -291, -292, -293, -294, -295, -296, -297, -298, -299, -300, 301, -302, -303, -304, -305, -306, -307, 308, -309, -310, -311, -312, -313, -314, -315, -316, -317, 318, -319, -320, -321, -322, -323, -324, -325, -326, -327, 328, -329, -330, -331, -332, -333, -334, 335, -336, -337, -338, -339, -340, -341, -342, -343, -344, -345, -346, -347, 348, -349, -350, -351, -352, -353, -354, -355, -356, -357, -358, 359, -360, -361, -362, -363, -364, 365, -366, -367, -368, -369, -370, -371, 372, -373, -374, -375, -376, -377, -378, -379, -380, -381, -382, -383, -384, 385, -386, -387, -388, -389, -390, -391, -392, -393, -394, -395, 396, 397, -398, -399, -400, -401, -402, -403, -404, -405, -406, -407, -408, -409, -410, -411, 412, -413, -414, 415, -416, -417, -418, -419, -420, -421, -422, -423, -424, -425, 426, -427, -428, -429, -430, -431, -432, -433, -434, -435, -436, -437, -438, -439, -440, 441, -442, 443, -444, -445, -446, -447, -448, -449, -450, -451, -452, -453, 454, -455, -456, -457, -458, -459, -460, -461, -462, -463, -464, -465, -466, 467, -468, -469, -470, -471, -472, 473, -474, -475, -476, -477, -478, -479, -480, -481, -482, 483, -484, -485, -486, -487, -488, -489, -490, -491, -492, -493, -494, 495, -496, -497, -498, -499, -500, 501, -502, -503, -504, 505, -506, -507, -508, -509, -510, -511, -512, -513, -514, -515, -516, -517, 518, -519, -520, -521, -522, -523, -524, 525, -526, -527, -528, -529, -530, -531, -532, -533, -534, -535, -536, -537, 538, -539, -540, -541, 542, -543, -544, -545, -546, -547, -548, -549, -550, -551, -552, -553, -554, -555, -556, 557, -558, -559, -560, -561, 562, -563, -564, -565, -566, -567, -568, 569, -570, -571, -572, -573, -574, -575, -576, -577, -578, -579, -580, -581, -582, -583, 584, -585, -586, -587, -588, -589, -590, -591, 592, -593, -594, -595, -596, -597, 598, -599, -600, -601, -602, -603, 604, -605, -606, -607, -608, -609, -610, -611, -612, -613, -614, -615, -616, -617, -618, -619, -620, 621, -622, -623, -624, -625, -626, 627, -628, -629, -630, -631, -632, 633, -634, -635, -636, -637, -638, -639, -640, -641, -642, -643, 644, -645, -646, -647, -648, -649, -650, 651, -652, -653, -654, -655, -656, -657, -658, -659, -660, 661, -662, -663, -664, -665, -666, -667, -668, -669, -670, 671, -672, -673, -674, -675, -676, 677, -678, -679, -680, -681, -682, -683, -684, -685, -686, -687, -688, -689, -690, -691, 692, -693, -694, -695, -696, -697, -698, 699, -700, -701, -702, 703, -704, -705, -706, -707, -708, -709, -710, -711, -712, -713, -714, -715, -716, -717, 718, -719, -720, -721, -722, -723, -724, -725, -726, -727, -728, 729]

example: Grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


example2: Grid = [
    [0, 0, 0, 0, 2, 7, 5, 8, 0],
    [1, 0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 8, 1, 0, 0, 0, 0],
    [4, 0, 6, 3, 0, 1, 0, 0, 9],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 2, 0, 0, 0, 0, 3, 1, 0],
]


empty_grid: Grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#### fonctions fournies

def write_dimacs_file(dimacs: str, filename: str):
    with open(filename, "w", newline="") as cnf:
        cnf.write(dimacs)


def exec_gophersat(
    filename: str, cmd: str = "gophersat", encoding: str = "utf8") -> Tuple[bool, List[int]]:
    result = subprocess.run(
        [cmd, filename], capture_output=True, check=True, encoding=encoding
    )
    string = str(result.stdout)
    lines = string.splitlines()

    if lines[1] != "s SATISFIABLE":
        return False, []

    model = lines[2][2:-2].split(" ")

    return True, [int(x) for x in model]


#### fonction principale

def cell_to_variable (i : int, j : int, valeur : int):
    return i *81 + j * 9 + valeur +1

def variable_to_cell (variable : int):
    variable = variable-1
    i = variable // 81
    variable = variable % 81
    j = variable // 9
    variable = variable %9
    valeur = variable
    return (i,j,valeur)


def model_to_grid(model: Model, nb_vals: int = 9) -> Grid:
    grid = []
    for i in range (nb_vals):
        grid.append([])

    for valeur in model:
        if valeur > 0:
            i,j,val = variable_to_cell(valeur)
            grid[i].append(val+1)
    
    return grid

def at_least_one(variables: List[PropositionnalVariable]) -> Clause:
    clause = variables[:] # Fait une copie
    return clause

def unique(variables: List[PropositionnalVariable]) -> ClauseBase: # renvoie les pairs de toutes les variables non A ou non B, non A ou non C , non B ou non C
    clause_base = []
    clause_base.append(at_least_one(variables)) # AJoute la contrainte au moins 

    phrase = variables[:] # On copie la liste
    phrase = [x * (-1) for x in phrase ] # on met toutes les varaibles négatives
    for c in combinations(phrase,2):
        clause_base.append(list(c))
    
    return clause_base
    
def  create_cell_constraints() -> ClauseBase: # On renvoie la contrainte d'unicité pour toutes les cases du sudoku
    clause_base = []
    cases = []
    for i in range (81):
        cases = [x+ (i*9) for x in range(1,10)]
        clause_base = clause_base + unique(cases)
    return clause_base
        
def create_line_constraints() -> ClauseBase: # On renvoie la contrainte d'unicité pour toutes les lignes du sudoku
    clause_base = []
    lignes = []
    for i in range (9): # On souhaite avoir 1,10,19,28,37,46,55,64,73 pour la première ligne, on fait ça 81 fois
        for j in range (1,10):
            lignes = [ (x*9)+j + 81*i for x in range(9)]
            clause_base. append(at_least_one(lignes))
    return clause_base

def create_column_constraints() -> ClauseBase :
    clause_base= []
    colonnes = []
    for i in range (1,82):
        colonnes = [i + x*81 for x in range (9)]
        clause_base.append(at_least_one(colonnes))
    return clause_base

def create_box_constraints() -> ClauseBase: # retourne les contraintes d'unicité pour les carrés
    clause_base =[]
    carre = []
    for i in range (3):
        for j in range (3):
            for k in range ( 9):
                for l in range (3):
                    for m in range (3):
                        carre.append(cell_to_variable(i*3+l,j*3+m,k))
                clause_base.append(at_least_one(carre))
                carre = []
    return clause_base

def create_value_constraints(grid: Grid) -> ClauseBase: # renvoie les contraintes d'unicité pour les valeurs en fonction de la grille
    clause_base = []
    for i in range (9):
        for j in range (9):
            if grid[i][j] != 0:
                clause_base.append([cell_to_variable(i,j,grid[i][j]-1)])
    return clause_base

def  generate_problem(grid: Grid) -> ClauseBase: # renvoie l'ensemble des clauses pour un problème de sudoku avec une grille de départ
    base_clause = []
    base_clause = create_cell_constraints() + create_line_constraints() + create_column_constraints() + create_box_constraints() + create_value_constraints(grid)
    return base_clause


def clauses_to_dimacs(clauses: ClauseBase, nb_vars: int) -> str:
    """
    Convertit une liste de clauses en une chaîne de caractères au format DIMACS.
    """

    dimacs = f"p cnf {nb_vars} {len(clauses)}\n"

    for formule in clauses:
        for element in formule:
            dimacs += f"{element} "
        dimacs += "0\n"
    return dimacs


def solveur (grid: Grid, nb_vars:int, filename : str):
    dimacs = clauses_to_dimacs(generate_problem(example), 729)
    write_dimacs_file(dimacs, filename)
    result = exec_gophersat(filename)
    if result[0]:
        print("SAT")
        model = result[1]
        newgrid = model_to_grid(model)
        affichage_grille(grid,False)
        affichage_grille(newgrid, True)
    else:
        print("UNSAT")

def affichage_grille(grille: Grid, solution : bool, nb_vals : int = 9):
    if not solution:

        print("Problème initial\n")
        print("-------------------------")

        for i in range (int(sqrt(nb_vals))):
            for j in range(int(sqrt(nb_vals))):
                for x in range (int(sqrt(nb_vals))):
                    print("|",end=" ")
                    for y in range (int(sqrt(nb_vals))):
                        print(grille[j+i*3][y+x*3], end=" ")
                print("|")
            print("-------------------------")


    else:

        print("\nSolution\n") 
        print("-------------------------")

        for i in range (int(sqrt(nb_vals))):
            for j in range(int(sqrt(nb_vals))):
                for x in range (int(sqrt(nb_vals))):
                    print("|",end=" ")
                    for y in range (int(sqrt(nb_vals))):
                        print(grille[j+i*3][y+x*3], end=" ")
                print("|")
            print("-------------------------")

    return 

    

def main():
    # print(cell_to_variable(1, 3, 4))
    # print(variable_to_cell(1))
    # print(variable_to_cell(113))
    # print(variable_to_cell(729))
    #pprint(model_to_grid(model))


    #pprint(create_value_constraints(example))
    #print(generate_problem(example))
    #solveur(example,729,"sudoku.cnf")

    print(variable_to_cell(729))



if __name__ == "__main__":
    main()
