# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Headnode of the return list
        headNode = ListNode(0)
        # A pointer that moves around, note we don't want to use the 
        # headNode otherwise we will lose the starting point
        dummyPointer = headNode
        # A place hold for carry
        carry = 0
        
        # We need carry to be here in case l1 and l2 only have one element and
        # the addup is greater than 10
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            dummyPointer.next = ListNode(val % 10)
            dummyPointer = dummyPointer.next
            carry = val / 10
            # Move on to the next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        headNode = headNode.next
        
        return headNode