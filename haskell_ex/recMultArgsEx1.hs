-- Funcion para encontrar la potencia de un numero b elevado a e
potencia :: Int -> Int -> Int
potencia _ 0 = 1 -- Caso base: Cualquier numero elevado a cero es 1
potencia b e = b * potencia b (e-1)  -- Llamada Recursiva: la potencia es 
                                     -- la multiplicacion sucesiva de un
                                     -- numero b, e veces

prueba :: Int
prueba = potencia 2 4 -- Devuelve 2^4 = 16

main :: IO()
main = print prueba

