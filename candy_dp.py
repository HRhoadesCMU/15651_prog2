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
    while current_node > 0:
        current_node = parent(current_node)
        st[current_node] = st[left_child(current_node)] + st[right_child(current_node)]
    return st

def range_query(st, current_node, left_query, right_query, left_edge, right_edge):
    if (left_query <= left_edge) and (right_query >= right_edge ):
        return st[current_node]
    else:
        mid_point = (left_edge + right_edge) / 2
        #exclude left
        if (left_query >= mid_point):
            return range_query(st, right_child(current_node), left_query, right_query, mid_point, right_edge)
        #exclude right
        elif (right_query <= mid_point):
            return range_query(st, left_child(current_node), left_query, right_query, left_edge, mid_point)
        #include portions of both left and right
        else:
            left = range_query(st, left_child(current_node), left_query, right_query, left_edge, mid_point)
            right = range_query(st, right_child(current_node), left_query, right_query, mid_point, right_edge)
            return left + right

if __name__ == "__main__":
    parameters = input()
    houses = input()