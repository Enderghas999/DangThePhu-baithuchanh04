def push_max(a, value):
    a.append(value)
    i = len(a) - 1
    while i > 0:
        p = (i - 1) // 2
        if a[p] >= a[i]:
            break
        a[p], a[i] = a[i], a[p]
        i = p

def pop_max(a):
    if not a:
        raise ValueError('Đống rỗng')
    result = a[0]
    last = a.pop()
    if not a:
        return result
    a[0] = last
    i = 0
    while 2*i + 1 < len(a):
        left = 2*i + 1
        right = left + 1
        child = left
        # TODO: nếu right tồn tại và a[right] > a[left], gán child = right.
        if right < len(a) and a[right] > a[left]:
            child = right
        
        if a[i] >= a[child]:
            break
        a[i], a[child] = a[child], a[i]
        i = child
    return result

a = [20, 9, 15, 3, 7, 1, 2]
push_max(a, 18)
print('Sau thêm:', a)
print('Lấy:', pop_max(a), 'còn:', a)
# TODO: thêm ca tự kiểm có con phải lớn hơn con trái để kiểm dòng chọn child.
