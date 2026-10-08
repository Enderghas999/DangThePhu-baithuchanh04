TREES = [[[4, 7], [9, 2]], [[4, 7], [2, 9]]]

def alpha_beta(node, is_max, seen, alpha=-2e9, beta=2e9):
    if isinstance(node, int):
        seen.append(node)
        return node
    best = -2e9 if is_max else 2e9
    for child in node:
        value = alpha_beta(child, not is_max, seen, alpha, beta)
        # TODO: MAX lấy max(best, value), rồi tăng alpha.        
        # TODO: MIN lấy min(best, value), rồi giảm beta.
        #raise NotImplementedError("TODO: cập nhật giá trị và cận")
        if is_max:
            best = max(best, value)
            alpha = max(alpha, best)
        else:
            best = min(best, value)
            beta = min(beta, best)

        if beta <= alpha:
            # TODO: dùng break để bỏ các con chưa xét.
            break
            #raise NotImplementedError("TODO: cắt nhánh")
    return best

# Sau TODO: (4, 4 lá) rồi (4, 3 lá).
for tree in TREES:
    seen = []
    value = alpha_beta(tree, True, seen)
    print(value, len(seen), seen)
