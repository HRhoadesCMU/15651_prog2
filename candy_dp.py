import sys
max_val_cap = 1000000007 # final result is total value % max_val_cap

#optimal substructure of a valid substring: longest sequence to current index
# with a max value less than the value at the current index
"""
Choice: take house or pass
- take house: add value to total and increase max val seen to item val, val of k decreases
- don't take house: no change in value or max val, index increases


"""


if __name__ == "__main__":
    parameters = input()
    houses = input()