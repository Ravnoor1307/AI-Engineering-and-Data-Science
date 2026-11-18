import argparse

# make a parser object
parser = argparse.ArgumentParser(prog="square", description="Calculates the square of input number")

# add argument
parser.add_argument("number", type=int, help="Number on which square will be calculated")

# optional argument --> verbosity
parser.add_argument("-v", "--verbose", help="Increases verbosity of output",
                    action="count", default=0)


# parse the results
results = parser.parse_args()

number = results.number
verbose = results.verbose

def calculate_square(number, verbose):
    if verbose == 1:
        return f"{number}^2 = {number ** 2}"
    elif verbose >= 2:
        return f"Square of {number} is {number ** 2}"
    
    return number ** 2

print(calculate_square(number, verbose))

# print(verbose)

