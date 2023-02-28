

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 方法一
    def swap_pairs1(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next = b
            a.next = b.next
            b.next = a
            pre = a
        return self.next

    # 方法二
    def swap_pairs2(self, head):
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummy.next

    # 方案三
    def swap_pairs3(self, head):
        if not head or not head.next:
            return head
        new = head.next
        head.next = self.swap_pairs3(new.next)
        new.next = head
        return new