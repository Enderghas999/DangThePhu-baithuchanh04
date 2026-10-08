def cung_cay(a,b):
    if a is None or b is None: return a is None and b is None
    if a[0]!=b[0]: return False
    # TODO: kiểm cặp trái và cặp phải tương ứng.
    return cung_cay(a[1], b[1]) and cung_cay(a[2], b[2])    
    #raise NotImplementedError("so hình dạng con")
def la_cay_con(g,b):
    if b is None: return True
    if g is None: return False
    # TODO: cung_cay tại g hoặc tìm ở hai con.
    if cung_cay(g, b): return True
    return la_cay_con(g[1], b) or la_cay_con(g[2], b)
    #raise NotImplementedError("tìm cây con nguyên vẹn")

a=(8,(3,None,(6,None,None)),(10,None,None))
b=(3,None,(6,None,None));c=(3,None,None)
print("Mong đợi:B=True,C=False; hai rỗng=True")
try:
    print(la_cay_con(a,b),la_cay_con(a,c),cung_cay(None,None))
except NotImplementedError as e: print("TODO:",e)
