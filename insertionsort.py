#insertion sort
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key
arr= list(input().split())
for i in range(len(arr)):
  arr[i]= int(arr[i])
insertionSort(arr)
print(arr)