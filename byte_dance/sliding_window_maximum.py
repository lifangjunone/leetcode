import heapq


class Solution:
    def max_sliding_window(self, nums, k):
        self.heap = [(-nums[i], i) for i in range(k)]
        heapq.nlargest(k, self.heap)
        heapq.heapify(self.heap)
        max_list = [-self.heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(self.heap, (-nums[i], i))
            while self.heap[0][1] <= i-k:
                heapq.heappop(self.heap)
            max_list.append(-self.heap[0][0])
        return max_list
