start_list = [12, 3, 4, 10, 8]
end_list = []
if len(start_list) > 1:
    last_index = len(start_list) - 1
    end_list.append(start_list[last_index])
    end_list = end_list + start_list[:-1]
    print(end_list)
else:
    print(start_list)