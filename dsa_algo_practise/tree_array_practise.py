class TreeArray():
    def __init__(self, binary_tree_array: list, index: int):
        self.binary_tree_array = binary_tree_array
        self.index = index
        
    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2

    def pre_order(self, index):
        if index >= len(self.binary_tree_array) or self.binary_tree_array[index] is None:
            return []
        return [self.binary_tree_array[index]] + self.pre_order(self.left_child_index(index)) + self.pre_order(self.right_child_index(index))

    def in_order(self, index):
        if index >= len(self.binary_tree_array) or self.binary_tree_array[index] is None:
            return []
        return self.in_order(self.left_child_index(index)) + [self.binary_tree_array[index]] + self.in_order(self.right_child_index(index))

    def post_order(self, index):
        if index >= len(self.binary_tree_array) or self.binary_tree_array[index] is None:
            return []
        return self.post_order(self.left_child_index(index)) + self.post_order(self.right_child_index(index)) + [self.binary_tree_array[index]]

if __name__ == "__main__":
    binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']
    tree = TreeArray(binary_tree_array)
    print("Pre-order Traversal:", tree.pre_order(0))
    print("In-order Traversal:", tree.in_order(0))
    print("Post-order Traversal:", tree.post_order(0))