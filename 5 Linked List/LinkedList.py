from typing import Callable

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __add__(self, var):
        if isinstance(var, int):
            cur = self
            while var > 0 and cur:
                cur = cur.next
                var -= 1
            return cur
        else:
            raise TypeError("Unsupported data type for '+' operation")
    
    def __str__(self):
        return str(self.val)
    
def fromHeadNode(head: ListNode) -> str:
    if head == None :
        return "Empty Linked List"
    items = []
    cur_node = head
    while cur_node:
        items.append(str(cur_node.val))
        cur_node = cur_node.next
    return ' -> '.join(items)
        
class LinkedList:
    def __init__(self, data=None) -> None:
        self.head = None
        
        if data is None:
            return
        elif isinstance(data, ListNode):
            self.head = data
            cur = self.head
            while cur:
                cur = cur.next
            return
        elif isinstance(data, list):
            for element in data:
                self.push(element)
        else:
            raise TypeError("Unsupported data type for LinkedList initialization")
    
    def push(self, val) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = ListNode(val)

    def __validateindex(self, index: int) -> int:
        if not isinstance(index, int):
            raise "index must be int"
        
        if index >= 0:
            if index >= len(self):
                raise("Index out of range")
            return index
        else:
            if index < -len(self):
                raise("Index out of range")
            return index + len(self)
    
    def __getnode(self, index: int) -> ListNode:        
        index = self.__validateindex(index)
        
        cur_node = self.head
        while index > 0:
            cur_node = cur_node.next
            index -= 1
            
        return cur_node
    
    def insert(self, index: int, val: any) -> None:
        if not isinstance(index, int):
            raise "index must be int"
           
        if index >= len(self):
            self.push(val)
            return
        
        newNode = ListNode(val)
        if index < 0:
            index += len(self)
        
        if index <= 0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp_node = self.__getnode(index - 1)
            newNode.next = temp_node.next
            temp_node.next = newNode
    
    def delete(self, index: int) -> None:
        index = self.__validateindex(index)
        
        if index == 0:
            self.head = self.head.next
        else:
            temp_node = self.__getnode(index - 1)
            temp_node.next = temp_node.next.next
    
    def reverse(self) -> ListNode:    
        prev_node = None
        cur = self.head
        
        while cur:
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
        
        self.head = prev_node
    
    def getmiddle(head: ListNode) -> ListNode:
        if not head:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def sort(self, key: Callable[[any], any] = lambda x: x, reverse: bool = False):
        
        def merge_sort(head: ListNode, key: Callable[[any], any] = lambda x: x, reverse: bool = False):
        
            def merge(left: ListNode, right: ListNode, key: Callable[[any], any] = lambda x: x, reverse: bool = False):
                if not left:
                    return right
                if not right:
                    return left
                
                if reverse ^ (key(left.val) <= key(right.val)):
                    result = left
                    result.next = merge(left.next, right, key=key, reverse=reverse)
                else:
                    result = right
                    result.next = merge(left, right.next, key=key, reverse=reverse)
                return result
                    
            if not head or not head.next:
                return head
            
            middle = LinkedList.getmiddle(head)
            right = middle.next
            
            middle.next = None
            
            left = merge_sort(head, key=key, reverse=reverse)
            right = merge_sort(right, key=key, reverse=reverse)           
            
            return merge(left, right, key=key, reverse=reverse)
        
        self.head = merge_sort(self.head, key=key, reverse=reverse)
    
    def __len__(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length
    
    def __setitem__(self, index: int, val: any) -> None:
        self.__getnode(index).val = val  
    
    def __getitem__(self, index: int) -> any:
        return self.__getnode(index).val
    
    def __str__(self) -> str:
        if self.head == None :
            return "Empty Linked List"
        items = []
        cur_node = self.head
        while cur_node:
            items.append(str(cur_node.val))
            cur_node = cur_node.next
        return ' -> '.join(items)
            
if __name__ == "__main__":
    ll = LinkedList([3, 2])
    ll.push(12)
    ll.push(1)
    
    print(ll)
    ll.insert(2, 44)
    print(ll)
    
    # ll.delete(-5)
    print(ll)
    print(f"Length: {len(ll)}")
    
    ll.sort(reverse=True)
    print(ll)
    
    ll.reverse()
    print(ll)