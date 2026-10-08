DATA = [["đỏ", "có"], ["đỏ", "có"],
        ["xanh", "không"], ["xanh", "không"]]

def majority(labels):  # Hỗ trợ: hòa chọn nhãn theo từ điển.
    return max(sorted(set(labels)), key=labels.count)

def learn(rows, max_height, level=1):
    labels = [r[-1] for r in rows]
    if len(set(labels)) == 1:
        return labels[0]
    if level >= max_height:
        # TODO: trả majority(labels), không chia tiếp.
      return majority(labels)
        #raise NotImplementedError("TODO: lá tại giới hạn")
    groups = {}
    for r in rows:
        groups.setdefault(r[0], []).append(r)
    children = {}
    for value, group in groups.items():
        # TODO: children[value] nhận learn(group,max_height,level+1).
        children[value] = learn(group, max_height, level + 1)
        #raise NotImplementedError("TODO: tăng mức khi gọi cây con")

    return (0, children)

# Sau TODO: cao 1 là lá "có";
# cao 2 hỏi màu: đỏ->có, xanh->không.
print("Cao 1:", learn(DATA, 1))
print("Cao 2:", learn(DATA, 2))
