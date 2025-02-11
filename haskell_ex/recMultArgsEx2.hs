-- Funcion para verificar si en una lista se encuentra un valor
isThere :: Eq a => a -> [a] -> Bool
isThere x [] = False -- Caso base: se tiene una lista vacia, por lo que el 
                     -- elemento x no esta en la lista
isThere x (y:ys) | x == y = True
                 | otherwise = isThere x ys -- Llamada recursiva: se extrae el  
                                            -- primer valor de la lista y se 
                                            -- compara con el valor buscado. El  
                                            -- valor de extraido se elimina.

prueba :: Bool
prueba = isThere 3 [1,2,3,4,5] -- Devuelve True

main :: IO()
main = print prueba

