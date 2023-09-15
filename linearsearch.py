def search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1
arr = list(input('Enter array values:\t').split())
for i in range(len(arr)):
  arr[i]=int(arr[i])
key=int(input('Enter element to search for:'))
print('Element found at',search(arr,key),'index')