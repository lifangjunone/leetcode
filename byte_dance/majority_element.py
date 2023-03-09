from collections import Counter


class Solution:

    def majorityElement(self, nums):
        mapping = {}
        max = 0
        max_key = nums[0]
        for item in nums:
            mapping[item] = mapping.get(item, 0) + 1
        for key, value in mapping.items():
            if value > max:
                max = value
                max_key = key
        return max_key

    def majorityElement2(self, nums):
        return Counter(nums).most_common(1)[0][0]

    def majorityElement3(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement4(self, nums):
        p = {}
        for item in nums:
            p[item] = p.get(item, 0) + 1
            if len(nums) / 2 < p[item]:
                return item
