class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        buy = []
        sell = []
  
        for p,a,t in orders:
            if t == 1:
                heappush(sell,(p,a))
            else:
                heappush(buy,(-p,a))

            while buy and sell:
                x, n = heappop(buy)
                y, m = heappop(sell)
            
                if -x >= y:
                    if n > m:
                        heappush(buy,(x,n-m))
                    elif n < m:
                        heappush(sell,(y,m-n))                       
                else:
                    heappush(buy,(x,n))
                    heappush(sell,(y,m))
                    break

        return sum(a for _, a in buy + sell) % (10**9 + 7)
