from typing import Generator

Interpretation = dict[str, bool]


def decomp(n: int, nb_bits: int):
    List = []
    reste = 0
    for _ in range(0, nb_bits):
        List.append(n % 2 != 0)
        n = n // 2

    return List


def interpretation(voc: list[str], vals: list[bool]) -> Interpretation:
    Dic = {}
    indice = 0
    for valeur in voc:
        Dic[valeur] = vals[indice]
        indice = indice + 1
    return Dic


def gen_interpretations(voc: list[str]) -> Generator[dict[str, bool], None, None]:
    donnee = []
    for valeur in range(2 ** len(voc)):
        donnee = decomp(valeur, len(voc))
        yield interpretation(voc, donnee)

def valuate (formula: str, interpretation : dict[str, bool]) -> bool:
    return eval(formula,interpretation)


def table_de_verite (formule : str, vocab : list[str]) -> list[bool]:
    table_verite = []
    resultat = True
    print(f"formule : {formule}")

    for i in gen_interpretations(vocab):
        resultat= valuate(formule,i)

        table_verite.append(resultat)
    return table_verite


def table_s (formule : str, vocab : list[str]) -> list[bool]:
    table_s = []
    resultat = True
    print(f"formule : {formule}")

    print("+---+---+---+-------+")
    print("|", end="")
    for v in vocab:
        print(f" {v} |", end = "")
    print(" eval. |")
    print("+---+---+---+-------+")


    
    for i in gen_interpretations(vocab):
        resultat= valuate(formule,i)

        print("|", end = "")
        for variable in vocab:
            print(f" {lettre(i[variable])} |",end="")

        print(f"   {lettre(resultat)}   |")

        table_s.append(resultat)
        #print(f"{i}--> {valuate(formule,i)}")
    print("+---+---+---+-------+")
    return table_s

def lettre (variable : bool) -> str:
    if variable:
        return "T"
    else :
        return "F"
    

def valide ( formule : str, vocab: list[str]) -> bool:
    for resultat in table_de_verite(formule,vocab):
        if resultat== False:
            return False
    return True

def contradictoire(formule : str, vocab: list[str]) -> bool:
    for resultat in table_de_verite(formule,vocab):
        if resultat== True:
            return False
    return True

def contingent(formule : str, vocab: list[str]) -> bool:
    memoire = False
    for resultat in table_de_verite(formule,vocab):
        if resultat== True:
            if memoire == False:
                memoire = True
            else:
                return True
    return False

def is_cons(f1: str, f2: str, voc: list[str]) -> bool:
    table1 = table_de_verite(f1, voc)
    table2 = table_de_verite(f2,voc)
    for i in range(len(table2)):
        if table1[i] and not table2[i]:
            return False
    return True

def main():
    # print(decomp(10,4))
    # print(interpretation(["A", "B", "C"],[True, True, False]))
    #for i in gen_interpretations(["toto", "tutu"]):
    #    print(i)
    #print(valuate("(A or B) and not(C)", {"A": True, "B": False, "C": False}))
    #table_s("(A or B) and not(C)",["A","B","C"])

    #voc = [f"x{i}" for i in range (20)]
    #print(valide("x1 or not(x1)",voc))

    #print(valuate("(A or B) and not(C)", {"A": True, "B": False, "C": False}))

    print(is_cons("A and B","A", ["A","B"]))


if __name__ == "__main__":
    main()
