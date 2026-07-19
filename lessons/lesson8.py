import math


def get_list_with_min_avg(input_data):
    def get_avg(input_list):
        if len(input_list) == 0:
            print("List is empty")
            return 0
        return sum(input_list) / len(input_list)

    min_avg = math.inf

    for num_list in input_data:
        current_avg = get_avg(num_list)
        if min_avg > current_avg:
            min_avg = current_avg

    return min_avg

data = [
    [1, 2],
    [3, 1],
    [0, 4],
]
print(get_list_with_min_avg(data))
