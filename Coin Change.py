class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a dp array to keep track of every index count
        dp = [amount+1 for i in range(amount+1)]
        # initialize it 0 index to 0 since if the amount is 0 result will yield 0
        dp[0] = 0
        # iterate over the 0 to amount and calculate every index
        for i in range(len(dp)):
            # iterate over the coins to calculate
            for j in coins:
                # if the needed coin is exacly in the coins list then 1 coin is enough for that amount
                if i==j:
                    dp[i] = 1
                    break
                # else if needed coin is more than instant coin calculate the minimum
                elif i-j>0:
                    dp[i] = min(dp[i], 1+dp[i-j])
        # amount of money cannot be made up by any combination of the coins return -1
        if dp[amount] == amount + 1:
            return -1
        # otherwise return the calculated value
        else:
            return dp[amount]


