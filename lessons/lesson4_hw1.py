arr = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
quant0 = arr.count(0)
arr1 = []
for i in range(0,len(arr)):
    if arr[i] != 0:
        arr1.append(arr[i])
arr1.extend([0] * quant0)
print(arr1)