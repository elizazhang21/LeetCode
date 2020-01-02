# 2. Add Two Numbers

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class addTwoNumbers(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        out = None
        while l1 is not None or l2 is not None:
            t1 = 0 if l1 is None else l1.val
            t2 = 0 if l2 is None else l2.val
            o = t1 + t2 + c
            if o >= 10:
                c = 1
                o = o - 10
            else:
                c = 0
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            node = ListNode(o)
            if out is None:
                out = node
                next = out
            else:
                next.next = node
                next = next.next

        if c == 1:
            next.next = ListNode(1)

        return out