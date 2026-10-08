class MinHeap:
    def __init__(self): self.a=[]
    def them(self,d,u):
        self.a.append((d,u))
        i=len(self.a)-1
        # TODO: đẩy lên theo ưu tiên.
        while i > 0:
            p = (i - 1) // 2
            if self.a[p][0] <= self.a[i][0]: break
            self.a[p], self.a[i] = self.a[i], self.a[p]
            i = p

    def lay(self):
        if not self.a: raise IndexError("heap rỗng")
        # TODO: giữ gốc, thay cuối, đẩy xuống.
        goc = self.a[0]
        cuoi = self.a.pop()
        if not self.a: return goc
        self.a[0] = cuoi
        i = 0
        while 2 * i + 1 < len(self.a):
            trai = 2 * i + 1
            phai = trai + 1
            nho = trai
            if phai < len(self.a) and self.a[phai][0] < self.a[trai][0]:
                nho = phai
            if self.a[i][0] <= self.a[nho][0]: break
            self.a[i], self.a[nho] = self.a[nho], self.a[i]
            i = nho
        return goc
    
def dijkstra(g,nguon):
    d={u:float("inf") for u in g}
    d[nguon]=0
    h=MinHeap();h.them(0,nguon)
    while h.a:
        du,u=h.lay()
        # TODO: bỏ bản cũ; thử du+w với từng cạnh.
        for v,w in g[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                h.them(d[v], v)
    return d
g={"A":[("B",4),("C",1)],"B":[("D",1)],
   "C":[("B",2),("D",5)],"D":[]}
print("Mong đợi:A0,B3,C1,D4")
try: print(dijkstra(g,"A"))
except NotImplementedError as e: print("TODO:",e)
