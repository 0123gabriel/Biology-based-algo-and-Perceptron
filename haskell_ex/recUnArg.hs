-- Función para sumar los digitos de un numero
sumaDigitos :: Int -> Int
sumaDigitos 0 = 0  -- El caso base es el numero 0 y la suma de digitos de 0 es 0
sumaDigitos n = n `mod` 10 + sumaDigitos (n `div` 10) -- Recursividad: suma del último dígito 
                                                      -- más la suma de los dígitos restantes

prueba :: Int
prueba  = sumaDigitos 23 -- Devuelve 5

main :: IO()
main = print prueba

