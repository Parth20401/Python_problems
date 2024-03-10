# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #if 1st node is to be deleted
        while(head != None and head.val == val):
            head = head.next

        if(head == None):
            return head

        res = head
        while head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return res
