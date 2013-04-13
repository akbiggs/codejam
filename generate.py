# generate.py
# Generates test cases for the problems.

import sys
import random

def generate_A(n):
    """
    Print out input representing n test cases for problem A.
    """

    print n
    for i in range(n):
        board = make_random_board()
        for row in board:
            print "".join(row)
        print

def make_random_board():
    board = []
    tomek = False
    for i in range(4):
        row = []
        for j in range(4):
            pieces = ["O", "X", "."] + (["T"] if not tomek else [])
            next_elt = random.choice(pieces)
            row.append(next_elt)
            
            # the tomek can only be placed once
            if next_elt == "T":
                tomek = True

        board.append(row)

    return board

if __name__ == "__main__":
    args = sys.argv[1:]
    generators = {"A": generate_A}
    if len(args) != 2:
        sys.stderr.write("usage: generate.py <problem> <num_tests>\n")
        sys.exit(1)
    
    problem, num_tests = args[0], int(args[1])
    if problem not in generators:
        sys.stderr.write("Invalid problem specified.\n")
        sys.exit(1)

    generator = generators[problem]
    generator(num_tests)
