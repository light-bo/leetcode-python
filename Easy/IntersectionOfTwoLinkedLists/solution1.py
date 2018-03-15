# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA
        while pa.next is not None:
            pa = pa.next

        pb = headB
        while pb.next is not None:
            pb = pb.next

        if pa != pb:
            return None

        pa = headA
        pb = headB

        while pa != pb:
            if pa.next is None:
                pa = headB
            else:
                pa = pa.next

            if pb.next is None:
                pb = headA
            else:
                pb = pb.next

        return pa
