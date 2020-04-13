# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''Problem Statement: https://leetcode.com/problems/intersection-of-two-linked-lists'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set=set()
        while headA != None:
            node_set.add(headA)
            headA=headA.next
        while headB != None:
            if headB in node_set:
                return headB
            else:
                node_set.add(headB)
            headB=headB.next
        return None
        
