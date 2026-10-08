def khoi_phuc(truoc,giua):
    if len(truoc)!=len(giua) or set(truoc)!=set(giua):
        raise ValueError("hai dãy không tương ứng")
    if len(set(truoc))!=len(truoc):
        raise ValueError("khóa phải phân biệt")
    if not truoc: return None
    goc=truoc[0]
    p=giua.index(goc)
    # TODO: dùng p chia hai dãy; gọi hai cây con.
    trai = khoi_phuc(truoc[1 : 1 + p], giua[:p])
    phai = khoi_phuc(truoc[1 + p :], giua[p + 1 :])
    # Trả tuple (goc,trai,phai).
    return (goc, trai, phai)

def sau(g):
    return [] if g is None else sau(g[1])+sau(g[2])+[g[0]]
truoc=[8,3,1,6,10];giua=[1,3,6,8,10]
print("Mong đợi duyệt sau:[1,6,3,10,8]")
try: print(sau(khoi_phuc(truoc,giua)))
except NotImplementedError as e: print("TODO:",e)
