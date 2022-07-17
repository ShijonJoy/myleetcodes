class Solution(object):
    def __init__(self) -> None:
        pass
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        match(n):
            case(0):
                return 0
            case(1):
                return 1
            case(2):
                return 1
            case _:
                return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)  

if __name__=="__main__":
    solution = Solution()
    print(solution.tribonacci(25))