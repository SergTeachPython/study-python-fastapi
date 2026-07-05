first_list = [[1, 2, 3], [4, 5, 6]]
tmp = first_list.copy()
print(id(first_list) == id(tmp))
print(id(first_list[0]) == id(tmp[0]))

#print(all([2 > 2, True, 5 == 5]))

#print(any([2 > 2, True, 5 < 5]))

# first_list = [2, 4, 7, 11 , '0', -2, 8]
# max(first_list)