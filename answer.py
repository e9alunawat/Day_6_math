"""Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum."""

from solver import solver


def answer():
    """Base Condition"""
    return solver(1, 100)


if __name__ == "__main__":
    print(answer())
