from selectionSort import numList
def bubble_sort(List):
	flag = False
	while not flag:
		flag = True
		for i in range(1, len(List)):
			if List[i] < List[i-1]:
				flag = False
				temp = List[i]
				List[i] = List[i-1]
				List[i-1] = temp
	
	return List


		
