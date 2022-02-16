class Solution:
    def reverse(self, x: int) -> int:
        result=0
        minus = False
        if x < 0:
            minus = True
            x = -1 * x

        while x!=0:

          if (result< pow(-2,31)/10) or (result > (pow(2,31)-1)/10):
            return 0

          result = result * 10 + x%10

          x //=10

        if minus:
            result = -1 * result

        return result
        