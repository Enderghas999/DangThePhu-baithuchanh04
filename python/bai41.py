class Fenwick:
    def __init__(self,a):
        self.a=a.copy();self.bit=[0]*(len(a)+1)
        for i,x in enumerate(a): self.cong(i,x)
    def cong(self,i,delta):
        j=i+1
        while j<len(self.bit):
            # TODO: cộng delta tại j, tiến j theo lowbit.
            self.bit[j] += delta
            j += j & (-j)
           #raise NotImplementedError("cập nhật block")
    def gan(self,i,moi):
        delta=moi-self.a[i];self.a[i]=moi
        self.cong(i,delta)
    def tien_to(self,r):
        j=r+1;total=0
        while j>0:
            # TODO: cộng block, giảm j theo lowbit.
            total += self.bit[j]
            j -= j & (-j)
            #raise NotImplementedError("tổng tiền tố")
        return total
    def doan(self,l,r):
        return self.tien_to(r)-self.tien_to(l-1)
print("Mong đợi:8,10,10")
try:
    f=Fenwick([2,1,4,3,5])
    print(f.doan(1,3))
    f.gan(2,6);print(f.doan(1,3))
    f.gan(2,6);print(f.doan(1,3))
except NotImplementedError as e: print("TODO:",e)
