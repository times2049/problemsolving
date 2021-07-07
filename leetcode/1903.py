class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(1,len(num)+1):
            if num[-i] in "13579":
                return num[:-i]+num[-i]
        return ""
