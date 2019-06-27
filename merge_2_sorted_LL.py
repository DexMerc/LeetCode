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
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            head = ListNode(l2.val)
            l2 = l2.next
        elif l2 == None:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            if l1.val >= l2.val:
                head = ListNode(l2.val)
                l2 = l2.next
            else:
                head = ListNode(l1.val)
                l1 = l1.next
        combi = head
        while l1!=None or l2!=None:
            if l1==None:
                combi.next = ListNode(l2.val)
                l2 = l2.next
            elif l2==None:
                combi.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val >= l2.val:
                    combi.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    combi.next = ListNode(l1.val)
                    l1 = l1.next
            combi = combi.next
        return head