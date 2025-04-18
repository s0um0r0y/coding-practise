from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ArrayInput:
	'''
	Dataclass to hold the inout array
	'''
	my_array: List[int] 
	n: int

class ArraySorter():
	def __init__(self,my_array):
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
	
	

if __name__ == "__main__":
	my_array = [64, 25, 12, 22, 11]
	array_sorter = ArraySorter(my_array)
	sorted_array_selection = array_sorter.selection_sort_array()
	print("selection sort : ",sorted_array_selection)
	sorted_array_bubble = array_sorter.bubble_sort_array()
	print("bubble_sort : ",sorted_array_bubble)


