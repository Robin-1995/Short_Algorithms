def prime_factors(n):

    def sieve_of_eratosthenes(n):
        nums = [x for x in range(3,n+1) if x%2!=0]
        primes = [2]
        i = 0
        while i<=n:
            if nums[i]**2 > n:
                break
            elif nums[i] != 0:
                for j in range(nums[i]**2,n+1,nums[i]):
                    if j < len(nums):
                        nums[j] = 0
            i += 1
        for val in nums:
            if val != 0:
                primes.append(val)
        return primes
