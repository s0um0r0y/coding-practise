class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right =None

    def preOrderTraversal(self, node):
        if node is None:
            return
        print(node.data, end = ", ")
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        print(node.data, end=", ")
        self.inOrderTraversal(node.right)

    def postOrderTraversal(self,node):
        if node is None:
            return
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node.data, end=", ")
    
    def left_child_index(self, index):
        return 2 * index + 1
    
    def right_child_index(self, index):
        return 2 * index + 2
    
    def get_data(self, index):
        if 0 <= index < len(self.node):
            return self.node[index]


if __name__ == "__main__":
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG

    print("root.right.left.data:", root.right.left.data)