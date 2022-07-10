from unicodedata import name


class Solution(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # if low % 2 !=0 and high % 2 ==0:
        #     count = (high -low + 1)/2
        # elif low % 2 ==0 and high % 2 !=0:
        #     count = (high- low +1)/2
        # elif low % 2 ==0 and high % 2 ==0:
        #     count = (high - low)/2
        # elif low % 2 !=0 and high % 2 !=0:
        #     count = (high-low)/2 + 1
        if bool(low%2)^bool(high%2):
            count = (high- low +1)/2
        elif low % 2 ==0 and high % 2 ==0:
            count = (high - low)/2
        elif low % 2 !=0 and high % 2 !=0:
            count = (high-low)/2 + 1

        return int(count)
        

if __name__ == "__main__":
    solution = Solution(2,5)
    print(solution.countOdds(3,7))