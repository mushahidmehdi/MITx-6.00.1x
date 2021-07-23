numList = [12, 23, 16, 69, 3, 78, 56, 45, 54, 65, 85, 15, 19, 91]

# Sorting the numList using Selection Sort

def selection_sort(List):
	index = 0
	while len(List) != index:
		for i in range(index, len(List)):
			if List[i] < List[index]:
				List[i], List[index] = List[index], List[i]

		index += 1
	return List


# print(selection_sort(numList))