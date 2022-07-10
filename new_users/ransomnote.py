class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)<=len(magazine):
            # do something
            for letter in ransomNote:
                if letter in magazine:
                    magazine = magazine[:magazine.find(letter)]+magazine[magazine.find(letter)+1:]
                    print(magazine)
                else:
                    return False
            if len(magazine) >=0:
                return True
        else:
            print('here')
            return False

solution = Solution()
print(solution.canConstruct('aab','baa'))