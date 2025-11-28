def BFS(root):
    queue = []
    queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(node.value)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)

# Example usage:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
if __name__ == "__main__":
    # Creating a sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    BFS(root)