"""
The goal of this class is to take an unsorted array and return the sorted array. This
class will take and store an array, held as a python list object (may change to np.array). 
The class will contain a variety of sorting methods that can be called.
https://www.geeksforgeeks.org/ <- useful source with nice implementations of algos
"""
class sorter():
	def __init__(self, arr):
		self.arr = arr
	def  insSort(self):
		"""
		This method will sort an array using insertion sort, this works by going through the array, starting from pos 1/ 2nd element
		if the current element (A) is less than the preceeding element B, B is shifted into position A. Then we go further left, until
		we reach a point in which A is bigger than or equal to that element.
		"""
		for i in range(1, len(self.arr)): 
			#going through array to get the value
			curr_val = self.arr[i] #holding the current value that needs to be sorted
			j = i-1
			#while there are more integers to look at execute loop
			while j >= 0:
				if self.arr[j] > curr_val:
					#if the preceding value is less than current value swap them, 
					#DOING TWO ASSIGNMENTS NOT BEST WAY TO DO IT.
					self.arr[j+1] = self.arr[j]
					#self.arr[j+1] = curr_val
				else:
					#if the preceeding value is less than or equal to the current_val break
					break
				j -= 1
			#good tip from
			#https://www.geeksforgeeks.org/insertion-sort/
			"""
			At a point where j = -1, so j+1 = start of array or the preceeding value is smaller than curr_Val, as a result we
			can set j+1 to curr_val
			"""
			print(j)
			self.arr[j+1] = curr_val
		return self.arr
	def bubbleSort(self):
		"""
		This method uses the bubble sort algorithm, where we look at sequential pairs and swap them if one is larger than the other. 
		This method iterates through the list making swaps. If no swaps can be made in the final sweep the sorting is done, so swaps need
		to be counted.
		"""
		swaps = 1
		#as long as swaps are made, we need to recheck the array
		while swaps > 0:
			print(swaps)
			#resetting swaps to zero
			swaps = 0
			for i in range(0, len(self.arr)-1):
				#checking if the bigger value preceeds a smaller value
				if self.arr[i] > self.arr[i+1]:
					#counting number of swaps made
					swaps +=1
					temp = self.arr[i] # storing the bigger val in temp
					self.arr[i] = self.arr[i+1] #replacing the left value with the smaller value
					self.arr[i+1] = temp #putting bigger value on right of pair
		return self.arr
	def selectionSort(self):
		start = 0
		while start < len(self.arr)-1:
			
			#start with whole array 
			#assume that the minimum value by default are the first index of the unsorted portion of array
			#storing both index and the minimum value
			min_val= self.arr[start]
			temp_indx = start
			print(start, min_val)
			# look up stream of starting position for values smaller than current start
			for i in range(start+1, len(self.arr)):
				#if there are smaller values update keep of track of their index and value
				if self.arr[i] < min_val:
					min_val = self.arr[i]
					temp_indx = i
			print(temp_indx, min_val)
			#swap start value with new minimum value
			temp_val = self.arr[start] #holding orginal starting value as temp
			self.arr[start] = min_val #replacing start of unsorted array with new min or original min
			self.arr[temp_indx] = temp_val #putting the starting value at the index of where the minimum was found
			start+=1
			print(self.arr)
				

def main():
	arr = [3,1,4,0,-4,4,2, 213]
	sortME = sorter(arr)
	sort = sortME.selectionSort()
	#print(sort)
main()