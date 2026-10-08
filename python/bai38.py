def cao(g):
    return 0 if g is None else 1+max(cao(g[1]),cao(g[2]))
def can(g):
    return 0 if g is None else cao(g[1])-cao(g[2])
def giua(g):
    return [] if g is None else giua(g[1])+[g[0]]+giua(g[2])
def quay_trai(g):
    # TODO: trả tuple mới, giữ cây con trung gian.
    p = g[2]
    return (p[0], (g[0], g[1], p[1]), p[2])
    #raise NotImplementedError("quay trái")
def quay_phai(g):
    t = g[1]
    return (t[0], t[1], (g[0], t[2], g[2]))
    #raise NotImplementedError("quay phải đối xứng")
def xoa_avl(g,x):
    if g is None: return None
    k,trai,phai=g
    # TODO: xóa đúng nhánh/0,1,2 con; nối lại tuple.
    if x < k:
        trai = xoa_avl(trai, x)
    elif x > k:
        phai = xoa_avl(phai, x)
    else:
        if trai is None: return phai
        if phai is None: return trai
        curr = phai
        while curr[1] is not None:
            curr = curr[1]
        k = curr[0]
        phai = xoa_avl(phai, curr[0])
    
    g = (k, trai, phai)
    
    # TODO: xét can(g), can(con); quay; trả gốc mới.
    b = can(g)
    if b > 1: 
        if can(g[1]) < 0:
            g = (g[0], quay_trai(g[1]), g[2])
        return quay_phai(g)
    if b < -1:
        if can(g[2]) > 0:
            g = (g[0], g[1], quay_phai(g[2]))
        return quay_trai(g)
    return g
    #raise NotImplementedError("xóa và cân bằng")

g=(4,(2,(1,None,None),(3,None,None)),(5,None,None))
print("Mong đợi:giữa[1,2,3,4],gốc2,cao3")
try:
    g=xoa_avl(g,5)
    print(giua(g),g[0],cao(g))
except NotImplementedError as e: print("TODO:",e)
