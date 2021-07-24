numList = [12, 23, 16, 69, 3, 78, 56, 45, 54, 65, 85, 15, 19, 91]


def selection_sort(arr):
	inspecting_index = 0
	while inspecting_index != len(arr):
		for i in range(inspecting_index, len(arr)):
			if arr[i] < arr[inspecting_index]:
				arr[i], arr[inspecting_index] = arr[inspecting_index], arr[i]
		inspecting_index += 1

	return arr

print(selection_sort(numList))