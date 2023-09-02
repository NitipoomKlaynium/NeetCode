class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
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

    root = TreeNode(arr[0])
    
    i = 2
    n = len(arr)
    left, right = [], []
    while i < n + 1:
        left += arr[i - 1: i - 1 + i//2]
        right += arr[i - 1 + i // 2: i * 2 - 1]
        i *= 2
    
    if left and left[0] is not None:
        root.left = listToTree(left)
    if right and right[0] is not None:
        root.right = listToTree(right)
    
    return root
      
def maxDepth(root: TreeNode, depth=1) -> int:
    if root is None:
        return 0

    l = maxDepth(root.left)
    r = maxDepth(root.right)
    
    return 1 + max(l, r)

def minDepth(root: TreeNode, depth=1) -> int:
    if root is None:
        return 0

    l = minDepth(root.left)
    r = minDepth(root.right)
    
    return 1 + min(l, r)
    
def diameterOfBinaryTree(root: TreeNode) -> int:
    if root is None:
        return 0
    print(maxDepth(root.left), maxDepth(root.right))
    return maxDepth(root.left) + maxDepth(root.right)
           
if __name__ == "__main__":
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # l = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    # l = [1,2,3,4,5,6,None,8]
    p = [1,2,1]
    q = [1,1,2]
    
    n1 = listToTree(p)
    n2 = listToTree(q)
    printTree(n1)
    printTree(n2)
    