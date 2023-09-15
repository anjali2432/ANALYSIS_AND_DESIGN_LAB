arr = input('Enter values\t').split()
for i in range(len(arr)):
  arr[i] = int(arr[i])
subarray = [] ; sum = 0
for i in  range(len(arr)):
  if arr[i]>0:
    subarray.append(arr[i])
    sum += arr[i]
print('The maximum sum of sub array\t',subarray,'is',sum)