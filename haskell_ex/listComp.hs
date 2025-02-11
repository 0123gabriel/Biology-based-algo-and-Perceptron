factors :: Int -> [Int]
factors n = [x | x <- [1..n], n `mod` x == 0]

resultado :: [Int]
resultado = factors 15 -- El resultado es [1,3,5,15]

prime :: Int -> Bool
prime n = factors n == [1,n]

answer :: Bool
answer = prime 15 -- El resultado es false

primes :: Int -> [Int]
primes n = [x | x <- [2..n], prime x] -- El resultado es [2,3,5,7]

result :: [Int]
result = primes 9

main :: IO()
main = print result