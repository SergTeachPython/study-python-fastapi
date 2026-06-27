initial_list = [1, 2, 3, 4, 5, 6]
#initial_list = [1, 2, 3]
#initial_list = [1, 2, 3, 4, 5]
#initial_list = [1]
#initial_list = []
end_list1 = []
end_list2 = []
end_list = []
length = len(initial_list)
if length == 1:
    end_list1 = initial_list
elif length % 2 == 0:
    len1 = int(length / 2)
    end_list1 = initial_list[:len1]
    end_list2 = initial_list[len1:]
elif length % 2 == 1:
    len1 = length // 2 + 1  # останній елемент не включається
    end_list1 = initial_list[:len1]
    end_list2 = initial_list[len1:]
end_list.append(end_list1)
end_list.append(end_list2)
print(end_list)
