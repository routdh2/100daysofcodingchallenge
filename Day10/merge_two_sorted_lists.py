# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''Problem Statement: https://leetcode.com/problems/merge-two-sorted-lists'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode(-1)
        ptr3=l3
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                ptr3.next=l1
                ptr3=ptr3.next
                l1=l1.next
            else:
                ptr3.next=l2
                ptr3=ptr3.next
                l2=l2.next
        if l1!=None:
            ptr3.next=l1
        if l2!=None:
            ptr3.next=l2
        return l3.next
        
        
