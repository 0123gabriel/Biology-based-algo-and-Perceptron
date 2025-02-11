% Se hace un tracking de la solucion preguntando por la posicion
% del granjero, cabra, lobo o col.
other_side(w,e).
other_side(e,w).

% Movimientos posibles. Cada lista tiene como variables al 
% granjero, lobo, cabra y col en ese orden.
% Los movimientos son que el granjero lleve a uno de los 
% animales o col, o no lleve a ninguno, y para representar 
% el cruce en el barco, la posicion inicial contendra un lado del
% rio (w ó e), y la final el otro (e ó w)
move([X,X,Goat,Cabbage],wolf,[Y,Y,Goat,Cabbage]):-other_side(X,Y). 
move([X,Wolf,X,Cabbage],goat,[Y,Wolf,Y,Cabbage]):-other_side(X,Y). 
move([X,Wolf,Goat,X],cabbage,[Y,Wolf,Goat,Y]):-other_side(X,Y). 
move([X,Wolf,Goat,Cabbage],nothing,[Y,Wolf,Goat,Cabbage]):-other_side(X,Y).

% Se chequea que las posiciones sean validas
safety_check(X,X,_). 
safety_check(X,_,X).

% Usando los predicados anteriores, se dice que se tiene una 
% posición segura si el hombre y la cabra estan del mismo lado,
% sin importar donde esta el lobo, y que es seguro el hombre y la col
% están del mismo lado sin importar donde este la cabra.
safe_status([Man,Wolf,Goat,Cabbage]):-safety_check(Man,Goat,Wolf), 
    								  safety_check(Man,Goat,Cabbage).

% Solucion cuando todos se encuentren del lado east. 
solution([e,e,e,e],[]).

% Llamada recursiva con la configuracion inicial. 
solution(Initial,[Move|OtherMoves]):-move(Initial,Move,NextInitial),
    								safe_status(NextInitial), 
    								solution(NextInitial,OtherMoves).