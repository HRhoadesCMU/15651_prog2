import sys
max_val_cap = 1000000007 # final result is total value % max_val_cap

"""
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
    return int((index-1)/2)

def left_child(index):
    return int(index*2 + 1)

def right_child(index):
    return int(index*2 + 2)

def assign(st, index, value):
    current_node = index + int((len(st)/2) - 1)
    st[current_node] = value
    while current_node > 0:
        current_node = parent(current_node)
        st[current_node] = st[left_child(current_node)] + st[right_child(current_node)]
    return st

def range_query(st, current_node, left_query, right_query, left_edge, right_edge):
    if ((left_query <= left_edge) and (right_query >= right_edge)):
        return st[current_node]
    elif (left_query > right_edge) or (right_query < left_edge):
        return 0
    else:
        mid_point = int((left_edge + right_edge) / 2)
        #exclude left
        if (left_query >= mid_point):
            return range_query(st, right_child(current_node), left_query, right_query, mid_point + 1, right_edge)
        #exclude right
        elif (right_query <= mid_point):
            return range_query(st, left_child(current_node), left_query, right_query, left_edge, mid_point)
        #include portions of both left and right
        else:
            left = range_query(st, left_child(current_node), left_query, right_query, left_edge, mid_point)
            right = range_query(st, right_child(current_node), left_query, right_query, mid_point, right_edge)
            return left + right

def range_sum(st, i, j):
    return range_query(st, 0, i, j, 0, int(len(st)/2))

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
    #n! / k! (n-k)!
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
    #print("n: " + str(n_fac) + " | k: " + str(k_fac) + " | n-k: " + str(n_minus_fac))
    print("n: " + str(n) + " | k: " + str(k) + " | n-k: " + str(n-k))
    ret_val = int(n_fac / (k_fac * n_minus_fac))
    print("ret val: " + str(ret_val))
    return ret_val


if __name__ == "__main__":
    parameters = input().split()
    houses = input().split()
    segTree_houses = build_segTree(len(houses))
    mapped_houses = map_values(houses)
    lis_table = [0 for i in range(0, len(houses))]
    total = 0
    #print(mapped_houses)
    for keys in mapped_houses:
        mapped_houses[keys].reverse()
        for indices in mapped_houses[keys]:
            lis_table[indices] = range_sum(segTree_houses, 0, indices) + 1
            assign(segTree_houses, indices, 1)
    for items in lis_table:
        k_val = int(parameters[1])
        print(type(items))
        if items >= k_val:
            total += n_choose_k(items, k_val)
    print(total)