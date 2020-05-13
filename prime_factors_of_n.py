def prime_factors(n):

    def sieve_of_eratosthenes(val):
        nums = [True for x in range(2,val+1)]
        primes = []

        i = 2
        while i<=n:
            if nums[i] == True:
                for j in range(i**2,val+1,i):
                    nums[i] = False
                i += 1
        for num in enumerate(nums):
            if nums[1] == True:
                primes.append(nums[0])
        return primes
