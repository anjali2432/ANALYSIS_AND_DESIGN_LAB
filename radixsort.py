def countSort(arr,exp):
  count = [0] * 10
  output = [0] * len(arr)
  for i in range(len(arr)):
    index=(arr[i]//exp)%10
    count[index]+=1
  for i in range(1,len(count)):
    count[i]+=count[i-1]
  i=len(arr)-1
  while i>=0 :
    index=(arr[i]//exp)%10
    output[count[index]-1]=arr[i]
    count[index]-=1
    i-=1
  for i in range(len(arr)):
    arr[i]=output[i]
def radixSort(arr):
  max1 = max(arr)
  exp=1
  while max1//exp>0:
    countSort(arr,exp)
    exp*=10
arr=list(input('Enter array values:\t').split())
for i in range(len(arr)):
  arr[i]=int(arr[i])
radixSort(arr)
print('Sorted array:\t',arr)