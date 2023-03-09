from math import pow


class Solution:
    def myPow(self, x, n):
        return pow(x, n)

    def myPow2(self, x, n):
        """
        x^n = x^1/2 * x^1/2
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow2(x, -n)
        if n % 2:
            return x * self.myPow2(x, n-1)
        else:
            return self.myPow2(x*x, n/2)

    def myPow3(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        p = 1
        while n:
            if n & 1:
                p *= x
            x *= x
            n >>= 1
        return p


if __name__ == '__main__':
    s = Solution().myPow3(2, 5)
    print(s)