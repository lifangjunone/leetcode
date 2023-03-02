import heapq


class KthLargest1:

    def __init__(self, k, nums):
        _heap = heapq.nlargest(k, nums)
        heapq.heapify(_heap)
        self.heap = _heap
        self.k = k

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


class KthLargest2:

    def __init__(self, k, nums):
        self.k, self.heap = k, heapq.nlargest(k, nums + [float("-inf")])
        heapq.heapify(self.heap)

    def __add__(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        heapq.heappushpop(self.heap, val)
        return self.heap[0]


if __name__ == '__main__':
    res = [float("-inf")]
    print(res)
    print(len(res))
    res = heapq.nlargest(4, [2, 5] + [float("-inf")])
    heapq.heapify(res)
    print(res)
    heapq.heappushpop(res, 3)
    print(res)
    heapq.heappushpop(res, 8)
    print(res)