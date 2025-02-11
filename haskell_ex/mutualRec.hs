-- Funcion para determinar si una vocal es mayuscula o minuscula
-- Arreglos de las vocales en mayusculas y minusculas para iterar sobre ellas
uppercase :: [Char]
uppercase = ['A', 'E', 'I', 'O', 'U']

lowercase :: [Char]
lowercase = ['a', 'e', 'i', 'o', 'u']

-- Se determina si la vocal es mayuscula
isUppercase :: Char -> [Char] -> [Char] -> Bool
-- Si es mayuscula se imprime True, si no se envia el arreglo de minusculas y se pregunta
-- si es minuscula
isUppercase c (x:xs) (y:ys) | c == x = True
                            | otherwise = isLowercase c xs (y:ys)
isUppercase _ _ _ = False -- Correccion de chatGPT: Caso que no coincide con nada

-- Se determina si la vocal es minuscula
isLowercase :: Char -> [Char] -> [Char] -> Bool
-- Si es minuscula se imprime True, si no se envia el arreglo de mayusculas y se pregunta
-- si es mayuscula
isLowercase c (x:xs) (y:ys) | c == y = True
                            | otherwise = isUppercase c (x:xs) ys
isLowercase _ _ _ = False -- Correccion de chatGPT: caso que no coincide con nada

prueba :: Bool
prueba = isUppercase 'E' uppercase lowercase

main :: IO()
main = print prueba




