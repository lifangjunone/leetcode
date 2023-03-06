import heapq
from collections import deque


class Solution:
    def max_sliding_window(self, nums, k):
        self.heap = [(-nums[i], i) for i in range(k)]
        heapq.nlargest(k, self.heap)
        heapq.heapify(self.heap)
        max_list = [-self.heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(self.heap, (-nums[i], i))
            while self.heap[0][1] <= i - k:
                heapq.heappop(self.heap)
            max_list.append(-self.heap[0][0])
        return max_list

    def max_sliding_window2(self, nums, k):
        win, res = [], []
        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k:
                win.pop(0)
            while win and nums[win[-1]] <= v:
                win.pop()
            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])
        return res

    def max_sliding_window3(self, nums, k):
        win, res = deque(), []
        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k:
                win.popleft()
            while win and nums[win[-1]] <= v:
                win.pop()
            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])
        return res


if __name__ == '__main__':
    s = Solution().max_sliding_window3(nums=[1, -1], k=1)
    print(s)
