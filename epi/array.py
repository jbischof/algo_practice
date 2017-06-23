import random
import numpy as np

def sort_even_odd(a):
	""" Function to sort array of ints by even/odd status """
	l = len(a)
	even_pos = 0
	odd_pos = l - 1
	while even_pos < odd_pos:
		# If even, move on
		if a[even_pos] % 2 == 0:
			even_pos += 1
		# If odd, swap out with unchecked entry
		else:
			a[even_pos], a[odd_pos] = a[odd_pos], a[even_pos]
			odd_pos -= 1
	return a

def pivot_cmp(a, pivot):
	""" Determines value of a given a pivot value for the Dutch national flag 
	problem. """
	if a < pivot:
		return 0
	if a == pivot:
		return 1
	if a > pivot:
		return 2

def swap_val(a, i, j):
	""" Swap values at indicies i and j in an array """
	a[i], a[j] = a[j], a[i]

def sort_pivot(a, i):
	""" Sort items in array according to relation to pivot
	Items less than pivot go first, equal second, greater than third
	Divide array into three regions:
	- less than pivot: [0 : less]
	- equal to pivot: [less : equal]
	- unsorted: [equal : high]
	- higher than pivot: [high : l - 1] 
	"""
	l = len(a)
	less = 0
	equal = 0
	high = l - 1
	pivot_val = a[i]
	while equal <= high:
		cmp_val = pivot_cmp(a[equal], pivot_val)
		# If less, swap to beginning, move less and equal forward
		if cmp_val == 0:
			swap_val(a, equal, less)
			equal += 1
			less += 1
		# If equal, move equal forward
		elif cmp_val == 1:
			equal += 1
		# If greater, move to end of array and move high index backwards
		elif cmp_val == 2:
			swap_val(a, equal, high)
			high -= 1

def four_int_sort(a):
	""" Sort array with values 0, 1, 2, 3 """
	l = len(a)
	less = 0
	equal = 0
	middle = l - 1
	high = l - 1
	while equal <= middle:
		cmp_val = a[equal]
		# If less, swap to beginning, move less and equal forward
		if cmp_val == 0:
			swap_val(a, equal, less)
			equal += 1
			less += 1
		# If equal, move equal forward
		elif cmp_val == 1:
			equal += 1	
		# If middle, move to end of middle section and move middle index
		elif cmp_val == 2:
			swap_val(a, equal, middle)
			middle -= 1
		# If greater, move to end of array and move high/middle index backwards
		# If middle < high, swap middle value with first unsorted
		elif cmp_val == 3:
			swap_val(a, equal, high)
			if middle < high:
				swap_val(a, equal, middle)
			high -= 1
			middle -= 1

def increment_pos_decimal(a):
	""" Increment a positive decimal integer represented an array """
	l = len(a)
	# Break off corner case where all numbers are 9
	if all([x == 9 for x in a]):
		return [1] + [0] * l
	# Otherwise can return array of same length
	pos = l - 1
	while pos >= 0:
		if a[pos] < 9:
			a[pos] += 1
			pos = -1
		if a[pos] == 9:
			a[pos] = 0
			pos -= 1
	return a


def shift_array(a, i):
	""" Shift items in array to the left on position i. 
	Add zero at end. """
	l = len(a)
	for j in range(i, l - 1):
		a[j], a[j + 1] = a[j + 1], a[j]
	a[l - 1] = 0

def shift_array_k(a, i, k):
	""" Shift items in array to the left k times on position i. 
	Add zeros at end. """
	l = len(a)
	while k > 0:
		shift_array(a, i)
		k -= 1
		i -= 1

def remove_dups_n2(a):
	""" Remove duplicates from sorted int array. 
	Returns the number of unique items. 
	This approach takes n2 time due to excessive shifting."""
	val_start = 0
	val_end = 0
	val = a[0]
	l = len(a)
	i = 1
	nunique = 1
	while i < l:
		# Another example of same value
		if a[i] == val:
			val_end = i
			i += 1
		# New value---reset counters and clean up dups
		else:
			nunique += 1
			ndups = val_end - val_start
			val_start = i
			val_end = i
			val = a[i]
			# Dups---shift everything leftward
			if ndups:
				# In interview might save this implementation for later
				shift_array_k(a, i - 1, ndups)
				l -= ndups
				i -= ndups
				val_start -= ndups
				val_end -= ndups
			# No dups!
			else:
				i += 1
	# Check for dups at very end
	ndups = val_end - val_start
	if ndups: 
		for i in range(val_start + 1, val_end + 1):
			a[i] = 0
	return nunique

def remove_dups(a):
	""" Remove duplicates from sorted int array. 
	Returns the number of unique items. """
	l = len(a)
	if l <= 1:
		return l
	# Index to place next unique 
	next_index = 1
	for i in range(1, l):
		if a[i] != a[next_index - 1]:
			# This is a new value, place at next index
			a[next_index] = a[i]
			next_index += 1
	return next_index

def enum_primes(x):
	""" Enumerate all prime numbers from 0 to x """
	if x < 2:
		return []
	primes = []
	for i in range(2, x):
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(i)
	return primes

def perm_array(a, perm):
	""" Permute array according to positions in 'perm' """
	# Current position in array
	for i in range(len(a)):
		p_pos = i
		p = perm[i]
		# Follow permutations in cycle 
		while perm[i] > 0:
			a[i], a[p] = a[p], a[i]
			perm[p_pos] = -1
			p_pos = p
			p = perm[p_pos]

def gen_random_int(a, b):
	""" Generate random integer from a to b """
	return a + int(random.random() * (b - a + 1))

def sample_offline(a, k):
	l = len(a)
	if k > l:
		raise ValueError('Cannot sample more items than in array.')
	for i in range(k):
		j = gen_random_int(i, l - 1)
		a[i], a[j] = a[j], a[i]

def reservior_samp(iterable, k):
	""" Function to sample k elements from an array of unknown length 
  Proof by induction the all items have same inclusion probability:
  	Base case: j = k. 
  		kth item has probability 1/l of being removed in round l. So probability
  		of being kept  in jth round is prod_{l=k+1}^{j} (l - 1) / l = 
  		k / (k + 1) * (k + 1) / (k + 2) * ... * (j - 2) / (j - 1) * (j - 1) / j =
  		k / j.
  	Generic case: jth item > k has inclusion probability k / j
  	Next case: After (j + 1)st round jth has inclusion probability 
  		(k / j) * j / (j + 1) = k / (j + 1)
	"""
	sample = []
	for i, val in enumerate(iterable):
		if i < k:
			sample.append(val)
		else:
			rint = gen_random_int(0, i)
			if rint < k:
				sample[rint] = val 
	return sample

def cum_prob_buckets(probs):
	""" Returns a list of N buckets of cumulative prob boundaries given a N-length
	array of probabilities. """
	cprobs = [0]
	total = 0
	for prob in probs:
		total += prob
		cprobs.append(total)
	# Make an array of buckets
	buckets = []
	for i in range(1, len(cprobs)):
		buckets.append([cprobs[i - 1], cprobs[i]])
	return buckets

def multinom_samp(N, probs):
	buckets = cum_prob_buckets(probs)
	sample = []
	for i in range(N):
		rand = random.random()
		for j, bucket in enumerate(buckets):
			if rand <= bucket[1] and rand > bucket[0]:
				sample.append(j)
	return sample

def spiral_array(a):
	""" Return array in list format using sprial order 
	Args:
	  a: a numpy array
	"""
	# Use number of columns as shape since empty array has one row and no cols
	l = a.shape[1]
	# Base cases
	if l == 0:
		return []
	elif l == 1:
		return [a[0, 0]]
	elif l == 2:
		return [a[0,0], a[0, 1], a[1,1], a[1, 0]]

	# Split off outer layer
	ret = []
	ret += a[0, ].tolist()
	ret += a[1:l, l-1].tolist()
	ret += a[l-1, 0:(l-1)][::-1].tolist()
	ret += a[1:(l-1), 0][::-1].tolist()

	# Recurse on inner matrix
	inner = a[1:-1, 1:-1]
	ret += spiral_array(inner)
	return ret

def rotate90_array(a):
	""" Rotate an array by 90 degrees.
	Time complexity: O(N)
	Space complexity: O(1)
	Args:
	  a: a numpy array
	"""
	l = a.shape[1]
	# Base case
	if l < 2:
		return

	# Process outer layer and recurse
	# L = last position in each dimension
	L = l - 1
	for i in range(L):
		a[0, i], a[i, L], a[L, L-i], a[L-i, 0] = \
		a[L-i, 0], a[0, i], a[i, L], a[L, L-i]

	rotate90_array(a[1:-1, 1:-1])
	return

