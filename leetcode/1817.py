class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        for i, t in logs:
            d[i].add(t)
        res = [0 for i in range(k)]
        for i in d:
            res[len(d[i])-1] += 1
        return res
