def nho_nhat(g):
    if g is None: return None
    while g[1] is not None:
        # TODO: cập nhật g sang trái.
        g = g[1]
        raise NotImplementedError("đi trái")
    return g[0]
def lon_nhat(g):
    if g is None: return None
    while g[2] is not None:
        g = g[2]
        raise NotImplementedError("đi phải")
    return g[0]
g=(8,(3,(1,None,None),None),(10,None,(14,None,None)))
print("Mong đợi: 1,14; rỗng:None")
try:
    print(nho_nhat(g),lon_nhat(g),nho_nhat(None))
except NotImplementedError as e: print("TODO:",e)
