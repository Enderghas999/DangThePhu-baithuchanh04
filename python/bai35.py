def truoc(g):
    stack,out=([g] if g else []),[]
    while stack:
        nut=stack.pop()
        # TODO: xuất gốc; đẩy con theo LIFO.
        out.append(nut[0])
        if nut[2] is not None: stack.append(nut[2])
        if nut[1] is not None: stack.append(nut[1])
        #raise NotImplementedError("duyệt trước vòng lặp")

    return out
def giua(g):
    stack,out=[],[]
    while g is not None or stack:
        # TODO: hạ trái, pop nút chờ, xuất, sang phải.
        while g is not None:
            stack.append(g)
            g = g[1]
        g = stack.pop()
        out.append(g[0])
        g = g[2]        
        #raise NotImplementedError("duyệt giữa vòng lặp")
    return out
def sau(g):
    stack,out=([(g,False)] if g else []),[]
    while stack:
        nut,da_mo=stack.pop()
        # TODO: cờ phân biệt lên lịch con và xuất gốc.
        if da_mo:
            out.append(nut[0])
        else:
            stack.append((nut, True))
            if nut[2] is not None: stack.append((nut[2], False))
            if nut[1] is not None: stack.append((nut[1], False))
        #raise NotImplementedError("duyệt sau vòng lặp")
    return out
g=(8,(3,None,None),(10,None,None))
print("Mong đợi:[8,3,10];[3,8,10];[3,10,8]")
for ham in [truoc,giua,sau]:
    try: print(ham(g))
    except NotImplementedError as e: print("TODO:",e)
