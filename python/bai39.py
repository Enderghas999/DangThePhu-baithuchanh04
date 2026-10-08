def tim(g,x):
    while g is not None:
        k,trai,phai=g
        if x==k: return True
        # TODO: chuyển g sang con đúng phía.
        g = trai if x < k else phai        
        #raise NotImplementedError("tìm BST/AVL")
    return False
bst=(1,None,(2,None,(3,None,(4,None,(5,None,None)))))
avl=(3,(2,(1,None,None),None),(4,None,(5,None,None)))
tap={1,2,3,4,5}
truy_van=[0,1,3,5,6]
print("Mong đợi cả ba:[False,True,True,True,False]")
try:
    print("BST:",[tim(bst,x) for x in truy_van])
    print("AVL:",[tim(avl,x) for x in truy_van])
    print("set:",[x in tap for x in truy_van])
except NotImplementedError as e: print("TODO:",e)
