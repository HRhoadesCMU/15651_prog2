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
"""
Implementation of segTree taken from Lecture 6 slides 15-17
"""
def build_segTree(size):
    tree = [0 for items in range(2*size)]
    return tree

def parent(index):
    return (index-1)/2

def left_child(index):
    return index*2 + 1

def right_child(index):
    return index*2 + 2

def assign(st, index, value):
    current_node = index + (len(st)/2) - 1
    st[current_node] = value
    while node > 0:
        node = (node-1)/2 #find parent


if __name__ == "__main__":
    parameters = input()
    houses = input()