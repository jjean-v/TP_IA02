import math
from typing import Callable
import pprint as pp
import ast
from random import randint

# Quelques structures de données

Grid = tuple[tuple[int, ...], ...]
State = Grid
Action = tuple[int, int]
Player = int
Score = float
Strategy = Callable[[State, Player], Action]

# Quelques constantes
DRAW = 0
EMPTY = 0
EMPTY_GRID: Grid = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
X = 1
O = 2


def grid_tuple_to_grid_list(grid: Grid) -> list[list[int]]:
    return list(list(ligne) for ligne in grid)


def grid_list_to_grid_tuple(grid: list[list[int]]) -> Grid:
    return tuple(tuple(ligne) for ligne in grid)


def legals(grid: State) -> list[Action]:
    list_action = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                list_action.append((i, j))
    return list_action


def check_row(grid: State, player: Player) -> bool:
    for ligne in grid:
        resultat = True
        indice = 0
        while resultat and len(ligne) > indice:
            if ligne[indice] != player:
                resultat = False
            indice += 1

        if resultat:
            return resultat
    return resultat


def check_column(grid: State, player: Player) -> bool:
    for i in range(len(grid)):
        resultat = True
        j = 0
        while resultat and len(grid) > j:
            if grid[j][i] != player:
                resultat = False
            j += 1

        if resultat:
            return resultat
    return resultat


def check_diago1(grid: State, player: Player) -> bool:
    i = 0
    resultat = True

    while resultat and len(grid) > i:
        if grid[i][i] != player:
            resultat = False
        i += 1

    return resultat


def check_diago2(grid: State, player: Player) -> bool:
    i = 0
    j = len(grid) - 1
    resultat = True

    while resultat == True and len(grid) > i:
        if grid[i][j] != player:
            resultat = False
        i += 1
        j -= 1

    return resultat


def line(grid: State, player: Player) -> bool:
    return (
        check_column(grid, player)
        or check_row(grid, player)
        or check_diago1(grid, player)
        or check_diago2(grid, player)
    )


def final(grid: State) -> bool:
    if line(grid, 1) or line(grid, 2) or legals(grid) == []:
        return True
    return False


def score(grid: State) -> Score:
    if line(grid, 1):
        return 1
    elif line(grid, 2):
        return -1
    else:
        return 0


def pprint(grid: State):
    chaine = ""
    for ligne in grid:
        for element in ligne:
            if element == 0:
                chaine += ". "
            elif element == 1:
                chaine += "X "
            else:
                chaine += "O "
        print(chaine)
        chaine = ""


def play(grid: State, player: Player, action: Action) -> State:
    if action in legals(grid):
        x, y = action
        grid_liste = grid_tuple_to_grid_list(grid)

        grid_liste[x][y] = player
        return grid_list_to_grid_tuple(grid_liste)
    return grid


def strategy(grid: State, player: Player) -> Action:
    list_action = legals(grid)
    # print(f"vous êtes les {player}")
    # pprint(grid)
    print("Choisissez un coup à jouer :")
    for i in range(len(list_action)):
        print(f"{i} : {list_action[i]}")
    coup = int(input("Saisir le numéro du coup que vous souhaitez jouer : "))
    return list_action[coup]


def strategy_brain(grid: State, player: Player) -> Action:
    print("à vous de jouer: ", end="")
    s = input()
    print()
    t = ast.literal_eval(s)

    return t


def tictactoe(strategy_X: Strategy, strategy_O: Strategy, alpha_beta : bool, debug: bool = False) -> Score:
    # Utiliser pour savoir si une stratégie alpha beta est utilisé, il faut donc rajouter des paramètres dans l'appel de la fonction
    grid = EMPTY_GRID
    current_player = X
    strategies = {X: strategy_X, O: strategy_O}
    # Pour le minmax
    alpha = -math.inf
    beta = math.inf
    while not final(grid):
        if debug:
            pprint(grid)

        if (alpha_beta):
            action_joueur = strategies[current_player](grid, current_player,alpha, beta)
        else :
            action_joueur = strategies[current_player](grid, current_player)

        grid = play(grid, current_player, action_joueur)

        if current_player == X:
            current_player = O
        else:
            current_player = X
    if debug:
        pprint(grid)

    return score(grid)


def strategy_first_legal(grid: State, player: Player) -> Action:
    return legals(grid)[0]


def strategy_random(grid: State, player: Player) -> Action:
    list_action = legals(grid)
    coup = randint(0, len(list_action))
    return list_action[coup]


## Joueur intelligent


def minmax(grid: State, player: Player) -> Score:
    if final(grid):
        return score(grid)
    elif player == X:
        best_value = -math.inf
        for coup in legals(grid):
            v = minmax(play(grid, X, coup), O)
            best_value = max(best_value, v)
        return best_value
    else:  # Player 0
        best_value = math.inf
        for coup in legals(grid):
            v = minmax(play(grid, O, coup), X)
            best_value = min(best_value, v)
        return best_value

def memoize(
    f: Callable[[State, Player], tuple[Score, Action]]
) -> Callable[[State, Player], tuple[Score, Action]]:
    cache = {} # closure
    def g(state: State, player: Player):
        if state in cache:
            return cache[state]
        val = f(state, player)
        cache[state] = val
        return val
    return g

@memoize
def minmax_action(grid: State, player: Player) -> tuple[Score, Action]:
    if final(grid):
        best_action = -1, -1
        return score(grid),best_action

    elif player == X:
        #best_coup = -1,-1
        best_value = -math.inf
        for coup in legals(grid):
            v,_ = minmax_action(play(grid, X, coup), O)
            if v > best_value:
                best_value = v
                best_action = coup    
        return best_value, best_action

    else:  # Player 0
        best_value = math.inf
        #best_coup = -1,-1
        for coup in legals(grid):
            v,_ = minmax_action(play(grid, O, coup), X)
            if v < best_value:
                best_value = v
                best_action = coup
        return best_value, best_action


def strategy_minmax(grid: State, player: Player) -> Action:
    _,action = minmax_action(grid,player)
    return action



@memoize
def minmax_actions(grid: State, player: Player) -> tuple[Score, list[Action]]:
    if final(grid):
        return score(grid), []

    best_actions = []
    
    if player == X:
        best_value = -math.inf
        for coup in legals(grid):
            v, _ = minmax_actions(play(grid, X, coup), O)
            if v > best_value:
                best_value = v
                best_actions = [coup]
            elif v == best_value:
                best_actions.append(coup)
        return best_value, best_actions

    else:  # player == O
        best_value = math.inf
        for coup in legals(grid):
            v, _ = minmax_actions(play(grid, O, coup), X)
            if v < best_value:
                best_value = v
                best_actions = [coup]
            elif v == best_value:
                best_actions.append(coup)
        return best_value, best_actions


def strategy_minmax_random(grid: State, player: Player) -> Action:
    _,list_action = minmax_actions(grid , player)
    return list_action[randint(0,len(list_action)-1)]


def memoize_alpha_beta(
    f: Callable[[State, Player], tuple[Score, Action]]
) -> Callable[[State, Player], tuple[Score, Action]]:
    cache = {} # closure
    def g(state: State, player: Player,a : float, b:float):
        if state in cache:
            return cache[state]
        val = f(state, player,a,b)
        cache[state] = val
        return val
    return g

@memoize_alpha_beta
def alpha_beta(grid: State, player: Player, alpha : float, beta : float) -> tuple[Score, Action]:
    if final(grid):
        best_action = -1, -1
        return score(grid),best_action

    elif player == X:
        #best_coup = -1,-1
        best_value = -math.inf
        for coup in legals(grid):
            v,_ = alpha_beta(play(grid, X, coup), O,alpha,beta)
            alpha = max(alpha,v)
            if alpha >= beta:
                best_value = v
                best_action = coup  
                break  
            if v > best_value:
                best_value = v
                best_action = coup    
        return best_value, best_action

    else:  # Player 0
        best_value = math.inf
        #best_coup = -1,-1
        for coup in legals(grid):
            v,_ = alpha_beta(play(grid, O, coup), X,alpha,beta)
            beta = min(v,beta)

            if alpha >= beta:
                best_value = v
                best_action = coup
                break
            if v < best_value:
                best_value = v
                best_action = coup
        return best_value, best_action


def strategy_alpha_beta(grid: State, player: Player, alpha: float, beta: float) -> Action:
    _,action = alpha_beta(grid,player, alpha, beta)
    return action


def main():
    GRID_1: Grid = ((0, 0, O), (0, X, 0), (0, 0, 0))
    # pprint(GRID_1)
    # strategy_brain(GRID_1,X)

    tictactoe(strategy_alpha_beta,strategy_alpha_beta, True, True)



if __name__ == "__main__" :
    main() 

 
