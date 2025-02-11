-- Sintaxis general: \argumento -> expresion
-- Ejemplo de una función que suma dos números
add :: Int -> (Int -> Int)
add x y = x + y

-- Uso de la función
resultado :: Int
resultado = add 3 4

-- Imprimir el resultado en la consola
main :: IO()
main = putStrLn $ "Resultado: " ++ show resultado
