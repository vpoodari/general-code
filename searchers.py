"""
This module contains a series of basic searching algorithms.
For general use.
Sources:
https://www.geeksforgeeks.org/searching-algorithms/ and subpages
"""
def linearSearch(arr, tar):
	"""
	Basic linear search, will search through the array/list one unit at a time, 
	until the element is found or an element greater than the element we are looking for is seen.
	"""
	for i in range(0, len(arr)):
		val = arr[i]
		if val == tar:
			return i
		elif val > tar:
			return -1
	#case where whole array was searched and no value was found
	return -1
def binarySearch(arr, tar, startI = 0):
	if len(arr) > 1:
		mid = (len(arr)-1)//2 #doing floor division so odd numbers are rounded down
		val = arr[mid]
		if val > tar:
			#print(found)
			arr = arr[0: mid+1]
			#print(arr)
			startI =startI+0
			return binarySearch(arr, tar, startI)
		elif val < tar:
			#print('in left')
			arr = arr[mid+1: ]
			#print(arr)
			startI = mid+1+startI
			return binarySearch(arr, tar, startI)
		if tar == val:
			#print('found')
			return startI+mid
	elif len(arr) == 1 and arr[0] == tar:
		return startI
	else:
		return -1 
def main():
	arr = [-3, -2, -1, 1, 2,3,5,6, 11, 17, 21, 22, 28 , 35, 42, 51]
	for i,c in enumerate(arr):
		print(i, c)
	print(binarySearch(arr, 42))

main()