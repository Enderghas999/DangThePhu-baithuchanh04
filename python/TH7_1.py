class Nut:
    def __init__(self,gt,trai=None,phai=None):
        self.gt,self.trai,self.phai=gt,trai,phai
def cao(g):
    return 0 if g is None else 1+max(cao(g.trai),cao(g.phai))
def chen(g,x):
    if g is None: return Nut(x)
    if x==g.gt: return g
    # TODO: chọn con, chèn đệ quy, nhận lại liên kết.
    raise NotImplementedError("chen BST")
def tim(g,x):
    while g is not None:
        if x==g.gt: return g
        # TODO: chuyển sang con đúng phía.
        raise NotImplementedError("tim BST")
    return None
def xoa(g,x):
    if g is None: return None
    # TODO: tìm nút; xử lý 0/1/2 con, dùng kế vị.
    raise NotImplementedError("xoa BST")
def giua(g):
    if g is None: return []
    # TODO: ghép dãy trái, khóa gốc, dãy phải.
    raise NotImplementedError("duyet giua")
def quay_trai(g):
    # TODO: giữ cây trung gian, đổi liên kết, trả gốc.
    raise NotImplementedError("quay trai")
def quay_phai(g):
    raise NotImplementedError("quay phai: đổi liên kết đối xứng")
def chen_avl(g,x):
    if g is None: return Nut(x)
    # TODO: chèn BST; xét balance; chọn TT/PP/TP/PT.
    raise NotImplementedError("chen AVL")
print("Mong đợi BST: [1,2,3,4,5,6,7]; AVL: gốc20,cao2")
try:
    g=None
    for x in [4,2,6,1,3,5,7]: g=chen(g,x)
    print(giua(g),tim(g,5).gt)
    print("Sau xóa4:",giua(xoa(g,4)))
    for ds in [[30,20,10],[10,20,30],[30,10,20],[10,30,20]]:
        a=None
        for x in ds: a=chen_avl(a,x)
        print(a.gt,cao(a))
except NotImplementedError as e: print("TODO:",e)
