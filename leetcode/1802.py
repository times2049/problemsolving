class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:


        result = 1
        maxSum -= n
        k = 1
        i = j = index
      
        while k <= maxSum:
            maxSum -= k
            result += 1
            if i == 0 and j == n-1:
                result += maxSum//k
                break
            elif i == 0:
                k += 1
                j += 1
            elif j == n-1:
                k += 1
                i -= 1
            else:
                i -= 1
                j += 1
                k += 2
        return result
