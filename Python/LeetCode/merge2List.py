# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode):
    placeholder = ListNode(0)
    current_node = placeholder
    
    while list1 != None or list2 != None:

        if list1 == None:
            current_node.next = list2
            break

        if list2 == None:
            current_node.next = list1
            break


        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next if list1 else None
        else:
            current_node.next = list2
            list2 = list2.next if list2 else None

        current_node = current_node.next

    return placeholder.next


first = ListNode()
second = ListNode(0)
mergeTwoLists(first, second)
        


    
