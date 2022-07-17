from array import array
from audioop import avg
from re import A


class Solution(object):
    def __init__(self) -> None:
        pass
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        return (sum(salary[1:-1]))/float(len(salary)-2)

if __name__ == "__main__":
    salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
    solution = Solution()
    print(solution.average(salary))

