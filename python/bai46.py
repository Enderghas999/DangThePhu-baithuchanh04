from math import log2  # Thư viện chuẩn.
DATA = [["đỏ", "nhỏ", "có"], ["đỏ", "lớn", "có"],
        ["xanh", "nhỏ", "không"], ["xanh", "lớn", "không"]]

def entropy(labels):
    if not labels:
        return 0.0
    counts = {}
    for x in labels:
        counts[x] = counts.get(x, 0) + 1
    result = 0.0
    for c in counts.values():
        p = c / len(labels)
        # TODO: result cộng -p * log2(p).
        result += -p * log2(p)
        #raise NotImplementedError("TODO: một hạng entropy")
    return result

def gain(rows, col):
    parent = entropy([r[-1] for r in rows])
    groups = {}
    for r in rows:
        groups.setdefault(r[col], []).append(r)
    for group in groups.values():
        # TODO: trừ entropy nhóm nhân len(group)/len(rows).
        parent -= (len(group) / len(rows)) * entropy([r[-1] for r in group])
        #raise NotImplementedError("TODO: entropy có trọng số")

    return parent

# Sau TODO: gain màu=1.0; gain cỡ=0.0.
print(gain(DATA, 0), gain(DATA, 1))
