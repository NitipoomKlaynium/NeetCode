import sys
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

from LinkedList import ListNode, LinkedList, fromHeadNode

def reverseList(head: ListNode) -> ListNode:    
    prev_node = None
    
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
        
    return prev_node
    
if __name__ == "__main__":
    l = LinkedList([1, 2])
    l2 = reverseList(l.head)
    # print(l2.next.next.next.next.next)
    print(fromHeadNode(l2))
    