def bang_ma(s):
    freq={c:s.count(c) for c in set(s)}
    nodes=[(f,c) for c,f in freq.items()]
    if not nodes: return {}
    while len(nodes)>1:
        nodes.sort(key=lambda x:x[0])
        f1,t1=nodes.pop(0);f2,t2=nodes.pop(0)
        # TODO: đưa (f1+f2,(t1,t2)) trở lại danh sách.
        nodes.append((f1 + f2, (t1, t2)))
    ma = {}
        #raise NotImplementedError("ghép hai nút nhỏ nhất")

    ma={}
    def ve(nut,p):
        if isinstance(nut,str): ma[nut]=p or "0";return
        # TODO: đi trái/phải, nối bit0/1.
        ve(nut[0], p + "0")
        ve(nut[1], p + "1")
        #raise NotImplementedError("gán mã theo cạnh")
    ve(nodes[0][1],"")
    return ma
def ma_hoa(s,ma):
    bits=[]
    for c in s:
        # TODO: thêm mã của c vào bits.
        bits.append(ma[c])
        #raise NotImplementedError("mã hóa ký tự")
    return "".join(bits)
def giai_ma(bits,ma):
    nguoc={v:k for k,v in ma.items()}
    out=[];p=""
    for b in bits:
        p+=b
        # TODO: nếu p khớp mã, xuất ký tự rồi reset p.
        if p in nguoc:
            out.append(nguoc[p])
            p = ""
        #raise NotImplementedError("đọc mã tiền tố")
    return "".join(out)
s="BANANA"
print("Mong đợi:3 mã,9 bit; giải mã=BANANA")
try:
    ma=bang_ma(s);bits=ma_hoa(s,ma)
    print(ma,bits,len(bits),giai_ma(bits,ma))
except NotImplementedError as e: print("TODO:",e)
