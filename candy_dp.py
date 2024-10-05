import sys
max_val_cap = 1000000007 # final result is total value % max_val_cap

"""
Implementation of segTree taken from Lecture 6 slides 15-17
"""
def build_segTree(size):
    tree = [(0,1) for items in range(2*size)]
    return tree

def parent(index):
    return int((index-1)/2)

def left_child(index):
    return int(index*2 + 1)

def right_child(index):
    return int(index*2 + 2)

def range_max(st, i, j):
    return range_max_query(st, 0, i, j, 0, int((len(st)-1)/2))

def assign_max(st, index, value, freq):
    current_node = index + int((len(st)-1)/2)
    st[current_node] = (value, freq)
    while current_node > 0:
        current_node = parent(current_node)
        left = st[left_child(current_node)]
        right = st[right_child(current_node)]
        if left[0] == right[0]:
            st[current_node] = (left[0], left[1] + right[1])
        elif left[0] > right[0]:
            st[current_node] = left
        else:
            st[current_node] = right
    return st

def range_max_query(st, current_node, left_query, right_query, left_edge, right_edge):
    #print("CN: " + str(current_node) + " | LQ: " + str(left_query) + " | RQ: " + str(right_query))
    #print("LE: " + str(left_edge) + " | RE: " + str(right_edge))
    if ((left_query <= left_edge) and (right_query >= right_edge)):
        return st[current_node]
    elif (left_query > right_edge) or (right_query < left_edge):
        return (0,1)
    else:
        mid_point = int((left_edge + right_edge) / 2)
        #exclude left
        if (left_query >= mid_point):
            return range_max_query(st, right_child(current_node), left_query, right_query, mid_point + 1, right_edge)
        #exclude right
        elif (right_query <= mid_point):
            return range_max_query(st, left_child(current_node), left_query, right_query, left_edge, mid_point)
        #include portions of both left and right
        else:
            left = range_max_query(st, left_child(current_node), left_query, right_query, left_edge, mid_point)
            right = range_max_query(st, right_child(current_node), left_query, right_query, mid_point, right_edge)
            if left[0] == right[0]:
                print(left[1] + right[1])
                return (left[0], left[1] + right[1])
            elif left[0] > right[0]:
                return left
            else:
                return right

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

def n_choose_k(n, k):
    counter = 1
    k_fac = 1
    n_minus_fac = 1
    if (k > n-k):
        while counter <= n-k:
            n_minus_fac = n_minus_fac * counter
            counter += 1
        k_fac = n_minus_fac
        while counter <= k:
            k_fac = k_fac * counter
            counter += 1
        n_fac = k_fac
    else:
        while counter <= k:
            k_fac = k_fac * counter
            counter += 1
        n_minus_fac = k_fac
        while counter <= k-n:
            n_minus_fac = n_minus_fac * counter
            counter += 1
        n_fac = n_minus_fac
    while counter <= n:
        n_fac = n_fac * counter
        counter += 1   
    return int(n_fac / (k_fac * n_minus_fac))

def fit_tree(input_length):
    counter = 0
    while (input_length/2 != 0) or (input_length%2 != 0):
        counter += 1
        input_length = int(input_length / 2)
    return 2**counter

def reset_tree(st):
    for i in range(0, int((len(st)/2)-1)):
        assign(st, i, 0)

if __name__ == "__main__":
    parameters = input().split()
    houses = input().split()
    n_val = int(parameters[0])
    k_val = int(parameters[1])
    segTree_houses = build_segTree(fit_tree(int(parameters[0])))
    mapped_houses = map_values(houses)
    lis_table = [(0,0) for i in range(0, n_val)]
    total = 0    

    for keys in mapped_houses:
        mapped_houses[keys].reverse()
        for indices in mapped_houses[keys]:
            #print("Ind: " + str(indices) + " | Key: " + str(keys))
            longest_increasing = range_max(segTree_houses, 0, indices)
            lis_table[indices] = (longest_increasing[0] + 1, longest_increasing[1])
            assign_max(segTree_houses, indices, lis_table[indices][0], lis_table[indices][1])
    print(lis_table)

    if k_val == 1:
        print(n_val)
    elif k_val > n_val:
        print(0)
    else:
        for items in lis_table:      
            if items[0] == k_val:
                total += items[1]
            elif items[0] > k_val:
                total = (total + (n_choose_k(items[0] + (items[1]-1), k_val) - n_choose_k(items[0] - 1, k_val))) % max_val_cap
        print(total)