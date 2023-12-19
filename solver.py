"""Find the difference between the sum of 
the squares of the consecutive natural numbers 
starting with and p and ending at q and 
the square of the sum of consecutive natural numbers starting with p and q."""


def solver(p, q):
    """Base Condition"""
    sol1 = [i**2 for i in range(p, q + 1)]
    sol1 = sum(sol1)
    sol2 = ((q * (q + 1)) / 2) ** 2
    result = sol2 - sol1
    return int(result)


if __name__ == "__main__":
    print(solver(1, 1000))
