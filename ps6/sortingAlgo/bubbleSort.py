from selectionSort import numList
print(numList)

def bubble_sort(arr):
	flag = False
	while not flag:
		flag = True
		for i in range(1, len(arr)):
			if arr[i] < arr[i-1]:
				temp = arr[i-1]
				arr[i-1] = arr[i]
				arr[i] = temp
				flag = False
	return arr

print(bubble_sort(numList))

		
