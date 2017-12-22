# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        if (l1 == None) and (l2 == None):
            return None

        p1 = l1
        p2 = l2
        result = None
        resultHead = None

        while (p1 != None) or (p2 != None):
            if p1 == None:
                while p2 != None:
                    resultHead.next = p2
                    resultHead = p2
                    p2 = p2.next
                break

            if p2 == None:
                while p1 != None:
                    resultHead.next = p1
                    resultHead = p1
                    p1 = p1.next
                break

            if p1.val >= p2.val:
                if result == None:
                    result = p2
                    resultHead = result
                else:
                    resultHead.next = p2
                    resultHead = p2

                p2 = p2.next
            else:
                if result == None:
                    result = p1
                    resultHead = result
                else:
                    resultHead.next = p1
                    resultHead = p1

                p1 = p1.next


        return result
