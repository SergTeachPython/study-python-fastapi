start_list = [12, 3, 4, 10, 8]
end_list = []
if len(start_list) > 1:
    end_list = start_list[-1:] + start_list[:-1]
    print(end_list)
else:
    print(start_list)