class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for i in range(len(accounts)):
            total = sum(accounts[i])
            max_wealth = max(max_wealth, total)

        return max_wealth
                      