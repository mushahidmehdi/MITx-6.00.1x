from selectionSort import numList

def merge(left, right):
	sorted_list = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sorted_list.append(left[i])
			i += 1
		else:
			sorted_list.append(right[j])
			j += 1
	while i < len(left):
		sorted_list.append(left[i])
		i += 1
	while j < len(right):
		sorted_list.append(right[j])
		j += 1
	return sorted_list

def merge_sort(arr):
	if len(arr) < 2:
		return arr[:]
	half = len(arr)//2
	left = merge_sort(arr[:half])
	right = merge_sort(arr[half:])
	return merge(left, right)