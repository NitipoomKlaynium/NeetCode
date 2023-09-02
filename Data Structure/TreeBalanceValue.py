class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Calculate sum of node values for a subtree rooted at `node`
def subtree_sum(node):
    if not node:
        return 0
    return node.value + subtree_sum(node.left) + subtree_sum(node.right)

# Rebalance tree based on node values
def balance_tree(node):
    if not node:
        return

    # Calculate the sums for left and right subtrees
    left_sum = subtree_sum(node.left)
    right_sum = subtree_sum(node.right)

    # If left subtree has a greater sum, rotate right (simplified)
    if left_sum > right_sum:
        tmp = node.left
        node.left = node.left.right
        tmp.right = node
        node = tmp

    # If right subtree has a greater sum, rotate left (simplified)
    elif right_sum > left_sum:
        tmp = node.right
        node.right = node.right.left
        tmp.left = node
        node = tmp

    # Recur for children
    balance_tree(node.left)
    balance_tree(node.right)


def displayTree(node: TreeNode, level=0):
    if node.right:
        displayTree(node.right, level + 1)
    print('\t' * level, node.value)
    if node.left:
        displayTree(node.left, level + 1)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(10)
    # Balance the tree
    displayTree(root)
    print("===========================")
    balance_tree(root)
    displayTree(root)