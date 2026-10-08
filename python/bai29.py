class Nut:
    def __init__(self,gt,trai=None,phai=None):
        self.gt,self.trai,self.phai=gt,trai,phai
def chen(g,x):
    if g is None: return Nut(x)
    if x==g.gt: return g
    if x < g.gt: 
        g.trai = chen(g.trai, x)
    else: 
        g.phai = chen(g.phai, x)
    return g

def tim(g,x):
    while g is not None:
        if x==g.gt: return g
        if x == g.gt: return g
        g = g.trai if x < g.gt else g.phai
    return None
   
def xoa(g,x):
    if g is None: return None
    # TODO: nối lại con; hai con dùng kế vị bên phải.
    if x < g.gt:
        g.trai = xoa(g.trai, x)
    elif x > g.gt:
        g.phai = xoa(g.phai, x)
    else:
        if g.trai is None: return g.phai
        if g.phai is None: return g.trai
        # Tìm kế vị bên phải (nhỏ nhất cây con phải)
        curr = g.phai
        while curr.trai is not None:
            curr = curr.trai
        g.gt = curr.gt
        g.phai = xoa(g.phai, curr.gt)
    return g

def duyet(g,kieu):
    if g is None: return []
    # TODO: ghép gốc và hai dãy con theo kieu.
    t = duyet(g.trai, kieu)
    p = duyet(g.phai, kieu)
    if kieu == "truoc": return [g.gt] + t + p
    if kieu == "giua":  return t + [g.gt] + p
    if kieu == "sau":   return t + p + [g.gt]
    return []


def thong_ke(g):
    if g is None: return (0,0,0)
    # TODO: trả (số nút,số lá,chiều cao).
    sn_t, sl_t, h_t = thong_ke(g.trai)
    sn_p, sl_p, h_p = thong_ke(g.phai)
    
    so_nut = 1 + sn_t + sn_p
    la_nut_la = (g.trai is None and g.phai is None)
    so_la = 1 if la_nut_la else (sl_t + sl_p)
    chieu_cao = 1 + max(h_t, h_p)
    
    return (so_nut, so_la, chieu_cao)
g=Nut(4,Nut(2,Nut(1),Nut(3)),Nut(6,Nut(5),Nut(7)))
print("Mong đợi: giữa1..7, thống kê(7,4,3); sau xóa1,2,4: [3,5,6,7]")
try:
    print(duyet(g,"giua"),thong_ke(g))
    for x in [1,2,4]: g=xoa(g,x)
    print(duyet(g,"giua"))
except NotImplementedError as e: print("TODO:",e)
