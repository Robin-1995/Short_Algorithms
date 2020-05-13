# Collatz Conjecture is a mathematical conjecture (unproved / not disproved theory) is a conjecture that states:
# for any number greater or equal to 1, following the sequence of: if even divide by 2, if odd multiply by 3 and add 1
# the sequence will always converge to 1


def collatz_conjecture(n):
    import matplotlib.pyplot as plt
    import pandas as pd
    i = 0
    yax = []

    try:
        if n == 0:
            raise ValueError
        else:
            while n > 1:
                yax.append(n)  # add the value of n to yax

                if n % 2 == 0:
                    n = n/2
                else:
                    n = 3*n+1
                i += 1

            # create a dataframe and plot n against i to show a graphically what the algorithm is doing
            yax.append(1)
            xax = [c for c in range(0, i+1)]
            df = pd.DataFrame(yax, index=xax)
            fig = df.plot.line(legend=False)
            fig.set_xlabel("term")
            fig.set_xlim((0, i))
            fig.set_ylabel("n")
            plt.show()

            return i

    except (TypeError, ValueError):
        print("Error: n must be an integer greater than 0")
