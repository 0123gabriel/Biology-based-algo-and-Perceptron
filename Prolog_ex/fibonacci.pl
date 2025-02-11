fibo(0,1).
fibo(1,1).
fibo(N,Y):-N > 1,
           C is N-1,
           D is N-2,
           fibo(C,A),
           fibo(D,B),
           Y is A+B.
