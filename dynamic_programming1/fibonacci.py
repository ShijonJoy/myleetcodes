class Solution(object):
    def __init__(self) -> None:
        pass
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        match(n):
            case(0):
                return 0
            case(1):
                return 1
            case _:
                return self.fib(n-1)+self.fib(n-2)  

if __name__=="__main__":
    solution = Solution()
    print(solution.fib(7))