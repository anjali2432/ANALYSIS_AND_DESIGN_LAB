def countingSort(arr):
  count = [0] * (max(arr)+1)
  output = [0] * len(arr)
  for i in arr:
    count[i]+=1
  for i in range(1,len(count)):
    count[i]+=count[i-1]
  i=len(arr)-1
  while i>=0:
    output[count[arr[i]]-1] = arr[i]
    count[arr[i]]-=1
    i-=1
  for i in range(len(arr)):
    arr[i]=output[i]
arr = list(input('Enter array values:\t').split())
for i in range(len(arr)):
  arr[i]=int(arr[i])
countingSort(arr)
print(arr)