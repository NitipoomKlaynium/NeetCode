class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)

def printTree(node: TreeNode, level=0) -> None:
    if node.right:
        printTree(node.right, level=level+1)
    print("\t" * level + str(node))
    if node.left:
        printTree(node.left, level=level+1)

def invertTree(node: TreeNode) -> None:
    if node.left:
        invertTree(node.left)
    if node.right:
        invertTree(node.right)
    node.left, node.right = node.right, node.left
    
def listToTree(arr: list):
    if not arr:
        return None

    # Find the middle of the array
    mid = len(arr) // 2

    # Create a root node
    root = TreeNode(arr[mid])

    # Recursively create the left and right subtrees
    root.left = listToTree(arr[:mid])
    root.right = listToTree(arr[mid+1:])

    return root
    
    

class Tree:
    def __init__(self, data=None) -> None:
        self.root = None
        
        if data is None:
            return
        elif isinstance(data, TreeNode):
            self.root = data
            return
        elif isinstance(data, list):
            self.root = listToTree(data)
        else:
            raise TypeError("Unsupported data type for LinkedList initialization")
        
    def __str__(self, level=0) -> str:
        return ""
        
        
if __name__ == "__main__":
    # n1 = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))
    n1 = listToTree([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])
    printTree(n1)
    invertTree(n1)
    print("=========================")
    printTree(n1)
    