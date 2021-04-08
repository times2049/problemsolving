class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int,set(re.sub('[a-z]',' ',word).split(' '))-{''})))
