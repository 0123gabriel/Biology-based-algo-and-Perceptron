-- Funcion para encontrar la cantidad de formas de tomar k elementos de un total de n elementos
comb :: Int -> Int -> Int
comb _ 0 = 1  -- Caso base: La cantidad de formas de tomar 0 elementos de un total de n elementos 
              -- es 1
comb n k | n == k = 1  -- Caso base: La cantidad de formas de tomar k elementos de un total de
                       -- de k = n elementos es 1
         | otherwise = comb (n-1) (k-1) + comb (n-1) k -- Llamada recursiva: propiedad de las
                                                       -- combinaciones

prueba :: Int
prueba = comb 15 5  -- Devuelve 6

main :: IO()
main = print prueba 

