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

#def longest_increasing_subset(st, )

def map_values(unsorted_house_list):
    value_map = {}
    temp_map = {}
    index_list = [list() for items in range(0, len(unsorted_house_list))]
    for i in range(0, len(unsorted_house_list)):
        if unsorted_house_list[i] not in temp_map:
            index_list[i].append(i)
            temp_map[unsorted_house_list[i]] = i
        else:
            index_list[temp_map[unsorted_house_list[i]]].append(i)
    sorted_list = unsorted_house_list
    sorted_list.sort()
    for j in range(0, len(sorted_list)):
        value_map[sorted_list[j]] = index_list[temp_map[sorted_list[j]]]
    return value_map

if __name__ == "__main__":
    parameters = input().split()
    houses = input().split()
    segTree_houses = build_segTree(len(houses))
    mapped_houses = map_values(houses)
    print(mapped_houses)
    #sorted_houses = houses
    #sorted_houses.sort()
    #mapped_houses = map_values(sorted_houses)
