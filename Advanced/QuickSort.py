def QuickSort(arr): 
	if len(arr) < 2 :
		return arr
	else:
		pivot = arr[0]
		less = [x for x in arr[1:] if x <= pivot]
		greater = [x for x in arr[1:] if x > pivot]
		sorted = [QuickSort(less) + [pivot] + QuickSort(greater)]
		return sorted
print(f"Sorted Array : {QuickSort([10534, 46522, 10014, 12459, 55462])}\n")
