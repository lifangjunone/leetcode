

def isValid1(s):
    """
    replace 替换
    :param s:
    :return:
    """
    while s:
        l = len(s)
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
        if len(s) == l:
            break
    return not s


def isValid2(s):
    """
    栈解法
    :param s:
    :return:
    """
    m = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for i in s:
        if i in m:
            stack.append(i)
        elif not stack or i != m[stack.pop()]:
            return False
    return not stack
