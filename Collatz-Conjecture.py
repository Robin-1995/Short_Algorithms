# Collatz Conjecture is a mathematical conjecture (unproved / not disproved theory) is a conjecture that states:
# for any number greater or equal to 1, following the sequence of: if even divide by 2, if odd multiply by 3 and add 1
# the sequence will always converge to 1


# this function returns the number of steps required to reach the value of 1
def collatz_conjecture(n):
    count = 0

    try:

        if n == 0:
            raise ValueError
        else:

            while n > 1:
                if n % 2 == 0:
                    n = n/2
                else:
                    n = 3*n+1
                count += 1
            return count
    except (TypeError, ValueError):
        print("Error: n must be an integer greater than 0")
