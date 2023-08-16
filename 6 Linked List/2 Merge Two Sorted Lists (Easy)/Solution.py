import sys
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

from LinkedList import ListNode, LinkedList, fromHeadNode

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    
    dummy = ListNode(-1)
    cur_node = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur_node.next, list1 = list1, list1.next
        else:
            cur_node.next, list2 = list2, list2.next
        cur_node = cur_node.next
        
    if list1:
        cur_node.next = list1
    else:
        cur_node.next = list2

    return dummy.next

if __name__ == "__main__":
        list1 = LinkedList([1, 2, 4])
        list2 = LinkedList([1, 3, 4])
        
        print(fromHeadNode(mergeTwoLists(list1.head, list2.head)))