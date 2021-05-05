class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res, avail = [], []
        tasks = sorted([(e, p, i) for i, (e, p) in enumerate(tasks)])
        i = 0
        time = tasks[0][0]
        while len(res) < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(avail, (tasks[i][1],tasks[i][2]))
                i += 1
            if avail:
                p, idx = heappop(avail)
                time += p
                res.append(idx)
            elif i < len(tasks):
                time = tasks[i][0]
        return res
