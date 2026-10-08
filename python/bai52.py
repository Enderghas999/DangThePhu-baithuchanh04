TREE = {"h": 0, "children": [
    {"h": 2, "children": [4, 7]},
    {"h": 5, "children": [1, 6]}
]}

def minimax_depth(node, depth, is_max):
    if isinstance(node, int):
        return node
    if depth == 0:
        # TODO: trả node["h"] vì nút chưa kết thúc.
        return node["h"]
        #raise NotImplementedError("TODO: điểm lượng giá")
    best = -2e9 if is_max else 2e9
    for child in node["children"]:
        value = minimax_depth(child, depth - 1, not is_max)
        # TODO: cập nhật best bằng max hoặc min theo is_max.
    best = max(best, value) if is_max else min(best, value)
        #raise NotImplementedError("TODO: gộp điểm con")
    return best

# Sau TODO: depth=1 -> 5; depth=2 -> 4.
for depth in [1, 2]:
    print(depth, minimax_depth(TREE, depth, True))
