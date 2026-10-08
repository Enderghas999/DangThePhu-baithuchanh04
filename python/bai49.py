DATA = [["đỏ", "có"], ["đỏ", "có"],
        ["xanh", "không"], ["đỏ", "không"]]
BOOT = [[0, 1, 2, 2], [0, 0, 1, 2], [3, 3, 2, 0]]

def majority(labels):
    return max(sorted(set(labels)), key=labels.count)

def learn_stump(rows):
    groups = {}
    for color, label in rows:
        groups.setdefault(color, []).append(label)
    tree = {}
    for color, labels in groups.items():
        # TODO: tree[color] = majority(labels).
        tree[color] = majority(labels)
        #raise NotImplementedError("TODO: lá của một màu")
    return tree

def vote(trees, color):
    counts = {}
    for tree in trees:
        label = tree[color]
        # TODO: tăng counts[label] một phiếu.
        counts[label] = counts.get(label, 0) + 1
        #raise NotImplementedError("TODO: đếm phiếu")
    return max(sorted(counts), key=counts.get)

trees = [learn_stump([DATA[i] for i in ids]) for ids in BOOT]
# Sau TODO: các phiếu ["có","có","không"]; kết quả "có".
print([t["đỏ"] for t in trees])
print(vote(trees, "đỏ"))
