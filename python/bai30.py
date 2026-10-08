def la_bst(g,lo=None,hi=None):
    if g is None: return True
    x,trai,phai=g
    # TODO: kiểm x nằm trong khoảng mở.
    if (lo is not None and x <= lo) or (hi is not None and x >= hi):
        return False
    # TODO: trái dùng (lo,x), phải dùng (x,hi).
    return la_bst(trai, lo, x) and la_bst(phai, x, hi)   

dung=(4,(2,(1,None,None),(3,None,None)),(6,None,None))
sai=(50,(30,None,(60,None,None)),(70,None,None))
print("Mong đợi: True, False")
try:
    print(la_bst(dung),la_bst(sai))
except NotImplementedError as e: print("TODO:",e)
