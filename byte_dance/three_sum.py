

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        l = len(nums)
        res = []
        for i in range(l-2):
            for j in range(i+1, l-1):
                for z in range(j+1, l):
                    result = nums[i] + nums[j] + nums[z]
                    r = (nums[i], nums[j], nums[z])
                    if result == 0 and r not in res:
                        res.append(r)
        return res

    def threeSum2(self, nums):

        map = set()
        nums = sorted(nums)
        l = len(nums)
        res = []
        for i in range(1, l-1):
            pre = nums[i-1]
            for j in range(i+1, l):
                map.add(pre)
                z = (nums[i] + nums[j])
                result = [-z, nums[i], nums[j]]
                if -z in map and result not in res:
                    res.append(result)
        return res

    def threeSum3(self, nums):
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            n = len(nums)
            left = i + 1
            right = n - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res > 0:
                    right -= 1
                elif res < 0:
                    left += 1
                elif res == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


if __name__ == '__main__':
    s = Solution().threeSum2([0,0,0])
    print(s)