"""

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""


def two_sum1(nums, target):
    """
    哈希表解法
    :param nums:
    :param target:
    :return:
    """
    mapping = {}
    for i, v in enumerate(nums):
        r = target - v
        if r in mapping:
            return [mapping[r], i]
        mapping[v] = i
    return []


def two_sum2(nums, target):
    """
    哈希表解法
    :param nums:
    :param target:
    :return:
    """
    mapping = {}
    for i, v in enumerate(nums):
        if v in mapping:
            return [mapping[v], i]
        mapping[target-v] = i
    return []


def two_sum3(nums, target):
    l = len(nums)
    for i in range(l-1):
        for j in range(1, l):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    return []


def main(nums, target):
    return two_sum3(nums, target)


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    res = main(nums, target)
    print(res)