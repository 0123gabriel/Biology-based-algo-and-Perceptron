% Estado con 3 canibales y 3 misioneros a la izquierda. Izquierda = 1
inicial(estado(3,3,1)).

% Estado con 3 canibales y 3 misioneros a la derecha. Derecha = 0
objetivo(estado(0,0,0)).

% Validacion de que no haya mas canibales que misioneros, ni mas de
% 3 misioneros, ni menos de 0. 
peligro(estado(NM,NC,_)) :- (NM < NC), (NM =\= 0).
peligro(estado(NM,NC,_)) :- (NM > NC), (NM =\= 3).

% Movimientos posibles y validacion del movimiento.
% Se usa "un" o "dos" para saber que cantidad de misioneros o 
% canibales se movieron, y "Dr" o "Iz" para saber hacia donde se
% hace el movimiento.
% mover un misionero a la derecha.
movimiento(estado(NM,NC,1),estado(NNM,NC,0),unMisioneroDr):- NNM is NM - 1,\+ peligro(estado(NNM,NC,0)),NM > 0.

% mover un misionero a la izquierda.
movimiento(estado(NM,NC,0),estado(NNM,NC,1),unMisioneroIz):- NNM is NM + 1,\+ peligro(estado(NNM,NC,1)),NM < 3.

% mover un canibal a la derecha.
movimiento(estado(NM,NC,1),estado(NM,NNC,0),unCanibalDr):- NNC is NC - 1,\+ peligro(estado(NM,NNC,0)), NC > 0.

% mover un canibal a la izquierda
movimiento(estado(NM,NC,0),estado(NM,NNC,1),unCanibalIz):- NNC is NC + 1,\+ peligro(estado(NM,NNC,1)), NC < 3.

% mover dos misioneros a la derecha
movimiento(estado(NM,NC,1),estado(NNM,NC,0),dosMisionerosDr):- NNM is NM - 2,\+ peligro(estado(NNM,NC,0)),NM > 1.

% mover dos misioners a la izquierda
movimiento(estado(NM,NC,0),estado(NNM,NC,1),dosMisonerosIz):- NNM is NM + 2,\+ peligro(estado(NNM,NC,1)),NM < 2.

% mover dos canibales a la derecha
movimiento(estado(NM,NC,1),estado(NM,NNC,0),dosCanibalDr):- NNC is NC - 2,\+ peligro(estado(NM,NNC,1)), NC > 1.

% mover dos canibales a la izquierda
movimiento(estado(NM,NC,0),estado(NM,NNC,1),dosCanibalIz):- NNC is NC + 2,\+ peligro(estado(NM,NNC,1)), NC < 2.

% mover un misionero y un canibal
movimiento(estado(NM,NC,0),estado(NNM,NNC,1),unMisioneroCanibalIz):- NNM is NM + 1, NNC is NC + 1,\+ peligro(estado(NNM,NNC,1)), NM < 3, NC < 3.

% mover un misionero y un canibal
movimiento(estado(NM,NC,1),estado(NNM,NNC,0),unMisioneroCanibalDr):- NNM is NM - 1, NNC is NC - 1,\+ peligro(estado(NNM,NNC,0)), NM > 0, NC > 0.

% Predicado para definir un movimiento posible
puede(Estado, Estado,_, []).

% Predicado recursivo para encontrar la solucion: se busca un
% movimiento i que sea posible y guie a la solucion, y luego a 
% partir de ese, se busca otro que sea posible y se repite este
% repite este proceso verificando que el estado inicial no se 
% repita para no caer en un bucle sin fin. Finalmente, cuando
% un movimiento i guia al estado final, se termina la recursividad y 
% se guardan los estados visitados como en un stack.
puede(EstadoX,EstadoY,Visitados, [Operador|Operadores]) :- movimiento(EstadoX, Estadoi, Operador),
	\+ member(Estadoi,Visitados),puede(Estadoi,EstadoY, [Estadoi|Visitados], Operadores).

consulta(Camino) :- inicial(Eini),objetivo(Efin), puede(Eini,Efin,[Eini],Camino).