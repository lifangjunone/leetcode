

def reverse_linked_list1(head):
    """
    双指针
    :param head:
    :return:
    """
    pre, cur = None, head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def reverse_linked_list2(head):
    """
    python 语法糖，类似于两数交换可以不使用第三个值
    :param head:
    :return:
    """
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


if __name__ == '__main__':
    reverse_linked_list2(head=None)