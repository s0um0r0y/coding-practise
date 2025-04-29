from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ArrayInput():
	'''
	Dataclass to hold the input array
	'''
	my_array: List[int] 
	n: int

class ArraySorter():
	def __init__(self,my_array: List[int], n: Optional[int] = None):
		self.my_array = my_array.copy()
		self.n = len(my_array)

	def selection_sort_array(self) -> List[int]:
		'''
		Selection sort
		input: 
			array of integers
		returns: 
			sorted array of integers
		'''
		for i in range(self.n-1):
			min_index = i
			for j in range(i+1, self.n):
				if self.my_array[j] < self.my_array[min_index]:
					min_index = j
			self.my_array[i], self. my_array[min_index] = self.my_array[min_index], self.my_array[i]
		return self.my_array

	def bubble_sort_array(self) -> List[int]:
		'''
		Bubble sort
		input: 
			array of integers
		return:
		 	sorted array of integers
		'''
		for i in range(self.n-1):
			swapped = False
			for j in range(self.n-i-1):
				if self.my_array[j] > self.my_array[j+1]:
					self.my_array[j], self.my_array[j+1] = self.my_array[j+1], self.my_array[j]
					swapped = True
			if not swapped:
				break
		return self.my_array
	
	def insertion_sort_array(self) -> List[int]:
		'''
		Insertion sort
		input:
			array of integers
		return:
			sorted array of integers
		'''
		for i in range(1, self.n):
			insert_index = i
			current_value = self.my_array.pop(i)
			for j in range(i-1, -1 ,-1):
				if self.my_array[j] > current_value:
					insert_index = j
			self.my_array.insert(insert_index, current_value)
		return self.my_array
	
	def quick_sort_array(self) -> List[int]:
		'''
		Quick sort
		input:
			array of integers
		return:
			sorted array of integers
		'''
		def partition(low: int , high: int) -> int:
			pivot = self.my_array[high]
			i = low -1

			for j in range(low, high):
				if self.my_array[j] < pivot:
					i += 1
					self.my_array[i], self.my_array[j] = self.my_array[j], self.my_array[i]

			self.my_array[i+1] , self.my_array[high] = self.my_array[high], self.my_array[i+1]
			return i+1
		
		def quick_sort(low: int, high: int):
			if high is None:
				high = self.n -1
			
			if low < high:
				pivot_index = partition(low, high)
				quick_sort(low, pivot_index-1)
				quick_sort(pivot_index+1, high)

		quick_sort(0, self.n-1)
		return self.my_array
	
	def counting_sort_array(self) -> List[int]:
		'''
		Counting sort
		input:
			array of integers
		return:
			sorted array of integers
		'''
		max_val = max(self.my_array)
		count = [0] * (max_val + 1)

		while len(self.my_array) > 0 :
			num = self.my_array.pop(0)
			count[num] += 1

		for i in range(len(count)):
			while count[i] > 0:
				self.my_array.append(i)
				count[i] -= 1
		
		return self.my_array
	
	def radix_sort_array(self) -> List[int]:
		'''
		Radix sort
		input:
			array of integers
		return:
			sorted array of integers
		'''
		radixArray: List[List[int]] = [[],[],[],[],[],[],[],[],[],[]]
		maxVal = max(self.my_array)
		exp = 1

		while maxVal // exp > 0:
			while len(self.my_array) > 0:
				val = self.my_array.pop()
				radixIndex = (val // exp) % 10
				radixArray[radixIndex].append(val)

			for bucket in radixArray:
				while len(bucket) > 0:
					val = bucket.pop()
					self.my_array.append(val)

			exp *= 10

		return self.my_array

	def merge_sort_array(self) -> List[int]:
		'''
		Merge sort
		input:
			array of integers
		return:
			sorted array of integers
		'''
		def mergeSort(my_array):
			if len(my_array) <= 1:
				return my_array
			
			mid = len(my_array) // 2
			leftHalf = my_array[:mid]
			rightHalf = my_array[mid:]

			sortedLeft = mergeSort(leftHalf)
			sortedRight = mergeSort(rightHalf)

			return merge(sortedLeft,sortedRight)
	
		def merge(left, right):
			result = []
			i = j = 0

			while i < len(left) and j < len(right):
				if left[i] < right[j]:
					result.append(left[i])
					i += 1
				else:
					result.append(right[j])
					j += 1

			result.extend(left[i:])
			result.extend(right[j:])

			return result
		
		return mergeSort(self.my_array)

		
if __name__ == "__main__":
	my_array = [64, 25, 12, 22, 11]
	array_sorter = ArraySorter(my_array, len(my_array))
	sorted_array_selection = array_sorter.selection_sort_array()
	print("selection sort : ",sorted_array_selection)
	sorted_array_bubble = array_sorter.bubble_sort_array()
	print("bubble sort : ",sorted_array_bubble)
	sorted_array_insertion = array_sorter.insertion_sort_array()
	print("insertion sort : ",sorted_array_insertion)
	sorted_array_quick = array_sorter.quick_sort_array()
	print("quick sort : ",sorted_array_quick)
	sorted_array_counting = array_sorter.counting_sort_array()
	print("counting sort : ",sorted_array_counting)
	sorted_array_radix = array_sorter.radix_sort_array()
	print("radix sort : ",sorted_array_radix)
	sorted_array_merge = array_sorter.merge_sort_array()
	print("merge sort : ",sorted_array_merge)

