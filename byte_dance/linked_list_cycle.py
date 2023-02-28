

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def hasCycle1(self, head):
        """
        快慢指针
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle2(self, head):
        """
        去重法
        :param head:
        :return:
        """
        s = set()
        cur = head
        while cur:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        return False


