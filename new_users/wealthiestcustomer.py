def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealths = []
        for i in accounts:
            wealth = 0
            for j in i:
                wealth += j
            wealths.append(wealth)
        return max(wealths)