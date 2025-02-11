mother(eve, abel).
mother(eve, cain).
father(adam, abel).
father(adam, cain).
parent(X,Y):-father(X,Y);mother(X,Y).
sibling(Y,Z):-parent(X,Y),parent(X,Z).
