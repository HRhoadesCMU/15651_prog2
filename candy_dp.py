import sys
max_val_cap = 1000000007 # final result is total value % max_val_cap

#optimal substructure of a valid substring: longest sequence to current index
# with a max value less than the value at the current index
"""
Choice: take house or pass
- take house: add value to total and increase max val seen to item val, val of k decreases
- don't take house: no change in value or max val, index increases

- segTree with range query gives max substring to index
- if equal/longer than k -> (val choose k) options, else next
"""

class segTree:
    def __init__(self, size, root):
        self.root = None
        self.size = size

class node:
    def __init__(self, index, value):
        self.index = index
        self.value = 0
        self.left = None
        self.right = None
        self.parent = None


def build_tree(size):
    st = segTree(size)
    for i in range (0,size):
        


if __name__ == "__main__":
    parameters = input()
    houses = input()