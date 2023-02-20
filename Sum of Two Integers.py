class Solution:
    def getSum(self, a: int, b: int) -> int:
        # while there is no carry bit do the same logic again and again
        a = a & (0xffffffff)
        while(b != 0):
            # take the xor of the two value
            sum = (a ^ b) & (0xffffffff)
            carry = ((a & b) << 1) & (0xffffffff)
            b = carry
            a = sum
        # If the result value is negative do bit manipulation
        if(a>>31) & 1:
            return ~(a^(0xffffffff))
        return a
