
nBienPlace([],[],0).

nBienPlace([T|R1], [T|R2], BP) :- 
    nBienPlace(R1,R2,B),
    BP is B + 1.
    
nBienPlace([T1|R1], [T2|R2], BP) :- 
    dif(T1, T2), 
    nBienPlace(R1,R2,BP).
    

longueur([],0).

longueur([_|R], N) :-
    longueur(R, X),
    N is X + 1.


gagne(C1,C2) :-
    nBienPlace(C1,C2,BP),
    longueur(C1,BP),
    longueur(C2,BP).

element(E,[E|_]).

element(E,[_|R]) :-
    element(E,R).

enleve(_,[],[]).

enleve(E,[E|R],R).

enleve(E,[T|R],[T|R2]) :-
    dif(E,T),
    enleve(E,R,R2).


enleveBP(X, X, [], []).
enleveBP([T|R1], [T|R2], C1, C2) :-
    enleveBP(R1, R2, C1 , C2).

enleveBP([T1|R1], [T2|R2], [T1|C1], [T2|C2]) :-
    dif(T1, T2),
    enleveBP( R1, R2, C1 , C2).
   

nMalPlacesAux([], _, 0).

nMalPlacesAux([T|R], L1, Res) :-
    element(T, L1),
    enleve(T, L1, L3),
    nMalPlacesAux(R, L3, N),
    Res is N + 1.

nMalPlacesAux([T|R], L2, Res):-
    \+element(T,L2),
    nMalPlacesAux(R, L2, Res).


nMalPlaces(L1, L2, Res) :-
    enleveBP(L1, L2, C1, C2),
    nMalPlacesAux(C1, C2, Res).

codeur(_, 0, []).

codeur(M, N, [H|Res]) :-
    N > 0,
    random(1, M, H),
    N2 is N-1,
    codeur(M, N2, Res).


% Question 4


affiche(0,_) :-
    write(" Tu n as plus de coup tu as perdu").

affiche(Max, X) :-
    Max >0,
    write("Il reste : "), write(Max), write(" coups"),
    nl,
    write(" Tapez un code : "),
    read(X),
    nl.


% Premier tour

tour1(Max, Code) :-
	affiche(Max, X),
    tour(Max, Code, X).


    
% Tour si il trouve le bon code

tour(Max, Code, X) :-
    Max > 0,
   	gagne(Code, X),
    nBienPlace(Code, X, BP),
    nMalPlaces(Code, X, MP),
    write("BP : "), write(BP), write("/MP : "), write(MP),
   	nl,
    write("Bravo tu as gagné ! ").

% tour classique

tour(Max, Code, X) :-
    Max > 0,
    nBienPlace(Code, X, BP),
    nMalPlaces(Code, X, MP),
    write("BP : "), write(BP), write("/MP : "), write(MP),
   	nl,
    Max2 is Max - 1,
    affiche(Max2,NewX),
    tour(Max2, Code, NewX).
    

jouons(M, N, Max) :-
    codeur(M, N, Code),
    tour1(Max, Code).
