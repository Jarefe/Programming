# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def removeAtIndex(self,index):
    #     if self.head is None:
    #         return
        
    #     if index == 0:
    #         self.removeFirstNode()
    #         return

    #     current_node = self.head
    #     position = 0
    #     while current_node is not None and current_node.next is not None and position + 1 != index:
    #         position +=1
    #         current_node = current_node.next

    #     if current_node is not None and current_node.next is not None:
    #         current_node.next = current_node.next.next
    #     else:
    #         print("Index not present")

def removeNthFromEnd(self, head, n):
    if head is None:
        return
    
    # dummy node is used in the case of n = 1; no need to implement removing head separately
    dummy = ListNode(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n+1):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
    

    

    
