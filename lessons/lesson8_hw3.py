def find_unique_value(some_list):
   temp_set = set(some_list)
   unique_list = list(temp_set)
   for i in range(len(unique_list)):
       if some_list.count(unique_list[i]) == 1:
           return unique_list[i]
           break


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
