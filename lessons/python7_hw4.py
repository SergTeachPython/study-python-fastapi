def common_elements():
    list_div_3 = set(range(0,100,3))
    list_div_5 = set(range(0, 100, 5))
    new_list = list_div_3.intersection(list_div_5)
    return new_list


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
