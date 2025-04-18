# You are given two non-empty linked lists representing two non-
# negative integers. The digits are stored in reverse order, and each of
# their nodes contains a single digit. Add the two numbers and return the
# sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1 : ListNode,l2 : ListNode):
    # Initialize new LL and related variables for the resulting sum
    placeholder = ListNode(0)
    current_node = placeholder
    carry = 0

    # Stop looping when there are no more nodes and no more carry value
    while l1 != None or l2 != None or carry != 0:
        # Check if node has value; if not then set to 0 
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0


        total_sum = l1Val + l2Val + carry # placed here because takes carry from previous iteration
        carry = total_sum // 10

        # Create new node and append to existing dummy head
        new_node = ListNode(total_sum % 10)
        current_node.next = new_node
        current_node = new_node

        # Check if next node exists
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # Return .next because first node holds no values
    return placeholder.next

    


l1 = [9,9,9,9,9,9,9]

l2 = [9,9,9,9]





