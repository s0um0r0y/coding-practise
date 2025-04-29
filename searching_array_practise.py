class searchingArray():
    def __init__(self, arr, targetVal):
        self.arr = arr
        self.targetVal = targetVal

    def binarySearch(arr, targetVal):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == targetVal:
                return mid
            
            if arr[mid] < targetVal:
                left = mid + 1
            else:
                right = mid - 1 

        return -1
    
if __name__ == "__main__":
    my_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    my_target = 15
    result = searchingArray.binarySearch(my_array,my_target)

    if result != -1:
        print("Value",my_target,"found at index", result)
    else:
        print("Target not found in array.")