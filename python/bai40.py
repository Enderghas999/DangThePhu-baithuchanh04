def day_xuong(a,i,n):
    while 2*i+1<n:
        # TODO: chọn con lớn hơn; đổi nếu cha nhỏ; tiến i.
        trai = 2 * i + 1
        phai = trai + 1
        lon = phai if (phai < n and a[phai] > a[trai]) else trai
        if a[i] >= a[lon]: break
        a[i], a[lon] = a[lon], a[i]
        i = lon
        #raise NotImplementedError("vun đống")

def heap_sort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1): day_xuong(a,i,n)
    for cuoi in range(n-1,0,-1):
        # TODO: đổi gốc/cuối rồi vun vùng còn lại.
        a[0], a[cuoi] = a[cuoi], a[0]
        day_xuong(a, 0, cuoi)
        #raise NotImplementedError("lấy cực đại")
def quick_sort(a,lo=0,hi=None):
    if hi is None: hi=len(a)-1
    if lo>=hi: return
    # TODO: chốt, phân hoạch và hai đoạn nhỏ hơn.
    chot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < chot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    quick_sort(a, lo, i - 1)
    quick_sort(a, i + 1, hi)
    #raise NotImplementedError("quick sort")
a=[7,2,9,1,5,3,8,4]
print("Mong đợi:[1,2,3,4,5,7,8,9]")
for ham in [heap_sort,quick_sort]:
    b=a.copy()
    try: ham(b);print(b)
    except NotImplementedError as e: print("TODO:",e)
