from selectionSort import numList

#def mergeSort(List):
#	if len(List) < 2:
#		return List
#	i = 0
#	j = 0
#	k = 0
#	middle = len(List)//2
#	left = List[:middle]
#	right= List[middle:]	
#	while i < len(left) or j < len(right):



def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1


