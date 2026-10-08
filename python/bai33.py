def tong_nut(g):
    if g is None: return 0
    x,trai,phai=g
    # TODO: cộng x và tổng hai con.
    return x + tong_nut(trai) + tong_nut(phai)
def tong_la(g):
    if g is None: return 0
    x,trai,phai=g
    if trai is None and phai is None: return x
    # TODO: nút trong chỉ chuyển tiếp tổng hai con.
    return tong_la(trai) + tong_la(phai)
g=(5,(-2,None,None),(9,(0,None,None),None))
print("Mong đợi: tổng nút12, tổng lá-2")
try: print(tong_nut(g),tong_la(g))
except NotImplementedError as e: print("TODO:",e)
