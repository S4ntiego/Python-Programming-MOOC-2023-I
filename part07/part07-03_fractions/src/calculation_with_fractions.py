# Write your solution here
import fractions


def fractionate(amount: int):
    final_fractions = []
    for i in range(amount):
        final_fractions.append(fractions.Fraction(numerator=1, denominator=amount))
    return final_fractions


if __name__ == "__main__":
    fractionate(5)
