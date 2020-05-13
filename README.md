# Short_Algorithms
A collection of short algorthims, written in python. These will updated as they are uploaded to GitHub

1) K_Closest_Points_to_Origin\
   this function takes in 2 arguments, list of coordinates (tuples) and k, where k is the number of coordinates to return (default = 1)\
   example: closest_points([(0,1),(2,2),(3,1),(1,1)],2) will return [(0,1),(1,1)]
  
2) Collatz-Conjecture\
   this function takes in a single argument (n) and returns the number of steps to converge to 1\
   the collatz conjecture states that for any value of n greater than 0 the following sequence will always converge to 1:\
   0th term = n\
   ith term is calculated using the following rule: if (i-1)th term is even, then divide by 2, else multiply by 3 and add 1
   
3) Prime_factors\
   this function takes in a single argument, n and returns a list of all prime factors of n\
   It uses the sieve of Eratosthenes algorithm to first determine all prime numbers up to and including n and then returns a subset of   these prime numbers, those that are factors of n
