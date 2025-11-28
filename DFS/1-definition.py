def depthFirstSearch(tree):
    if tree is None:
        return
    print(tree.value)

    for child in tree.children:
        depthFirstSearch(child)

# Example usage:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  
if __name__ == "__main__":
    # Creating a sample tree:
    #         1
    #       / | \
    #      2  3  4
    #     / \
    #    5   6

    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    root.children.extend([child1, child2, child3])
    child1.children.extend([TreeNode(5), TreeNode(6)])

    depthFirstSearch(root)