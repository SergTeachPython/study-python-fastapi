arr = []
sum = 0
for i in range(0,len(arr),2):
    sum += arr[i]
if len(arr)>0:
    sum *= arr[len(arr)-1]
else:
    sum = 0
print(sum)
