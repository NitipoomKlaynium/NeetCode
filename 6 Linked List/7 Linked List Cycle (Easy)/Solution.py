import sys
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

from LinkedList import LinkedList, ListNode

def hasCycle(head: ListNode) -> bool:

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
                
        return False
    
if __name__ == "__main__":
    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)