DATA = [["đỏ", "nhỏ", "có"], ["đỏ", "lớn", "có"],
        ["xanh", "nhỏ", "không"], ["xanh", "lớn", "không"]]

def gini(labels):
    if not labels:
        return 0.0
    counts = {}
    for x in labels:
        counts[x] = counts.get(x, 0) + 1
    total = 0.0
    for c in counts.values():
        # TODO: cộng (c / len(labels)) ** 2 vào total.
        raise NotImplementedError("TODO: bình phương xác suất")
    return 1.0 - total

def learn(rows, cols):
    labels = [r[-1] for r in rows]
    if len(set(labels)) == 1:
        return labels[0]
    if not cols:
        # TODO: trả nhãn đa số, hòa chọn nhãn nhỏ theo từ điển.
        raise NotImplementedError("TODO: lá đa số")
    candidates = []
    for col in cols:
        groups = {}
        for r in rows:
            groups.setdefault(r[col], []).append(r)
        score = 0.0
        for group in groups.values():
            # TODO: cộng len(group)/len(rows) * gini(nhãn nhóm).
            raise NotImplementedError("TODO: Gini có trọng số")
        candidates.append((score, col, groups))
    _, col, groups = min(candidates, key=lambda x: (x[0], x[1]))
    rest = [c for c in cols if c != col]
    return (col, {v: learn(g, rest) for v, g in groups.items()})

# Sau TODO: Gini gốc = 0.5; cây hỏi cột 0.
print(learn(DATA, [0, 1]))
