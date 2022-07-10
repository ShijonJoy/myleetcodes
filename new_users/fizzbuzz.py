class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5 !=0:
                answer.append("Fizz")
            elif (i+1)%5 == 0 and (i+1)%3 !=0:
                answer.append("Buzz")
            elif (i+1)%3 == 0 and (i+1)%5 ==0:
                answer.append("FizzBuzz")
            else:
                answer.append(str(i+1))
        return answer

fizzBuzz = Solution()
print(fizzBuzz.fizzBuzz(5))