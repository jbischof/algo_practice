# Sorting algorithms
def bubblesort(array):
	l = len(array)
	# Number of swaps in last pass
	swaps = 1
	while swaps > 0:
		# Set swap counter back to zero
		swaps = 0
		for i in range(l - 1):
			if array[i + 1] < array[i]:
				array[i], array[i + 1] = array[i + 1], array[i]
				swaps += 1

def mergearr(arr1, arr2):
	""" Merging util for merge sort. Both input arrays are assumed sorted. """
	ans = []
	while len(arr1) > 0 or len(arr2) > 0:
		if not arr2:
			ans.append(arr1.pop(0))
		elif not arr1:
			ans.append(arr2.pop(0))
		elif arr1[0] <= arr2[0]:
			ans.append(arr1.pop(0))
		else:
			ans.append(arr2.pop(0))
	return ans

def mergesort(array):
	# Base case: length 0 or 1
	l = len(array)
	if l < 2:
	  return array
	# Split array and sort
	mid = l / 2
	return mergearr(mergesort(array[: mid]), mergesort(array[mid: ]))

def swap_pivot(array, pivot_pos, swap_pos):
	# Swaps out value in array for value in front of pivot
	# Pivot placed in front of swapped value
	if pivot_pos <= swap_pos:
		return False
	move_pos = pivot_pos - 1
	array[swap_pos], array[move_pos] = array[move_pos], array[swap_pos]
	# Swap pivot with compared value
	array[pivot_pos], array[move_pos] = array[move_pos], array[pivot_pos]
	return True

def quicksort(array, low, high):
	#print array[low : min(high+1, len(array) - 1)]
	# Base case: array length < 2
	if low >= high:
		return
	pivot_pos = high
	pivot = array[pivot_pos]
	# Index of comparison
	i = low
	while pivot_pos > low and (pivot_pos - i > 0):
		# Keep comparing position i value to pivot until value is less
		while array[i] < pivot:
			# Move ith value behind pivot
			swap_pivot(array, pivot_pos, i)
			# New position of pivot
			pivot_pos -= 1
		i += 1
	quicksort(array, low, max(pivot_pos - 1, low))
	quicksort(array, min(pivot_pos + 1, high), high) 
