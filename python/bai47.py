DATA = [[1, "không"], [2, "không"], [4, "có"], [7, "có"]]

def gini(labels):
    if not labels:
        return 0.0
    return 1 - sum((labels.count(x)/len(labels))**2
                   for x in set(labels))

def best_threshold(rows):
    values = sorted({r[0] for r in rows})
    if len(values) < 2:
        raise ValueError("Không có ngưỡng")
    best_t, best_score = None, float("inf")
    for a, b in zip(values, values[1:]):
        t = (a+b)/2
        left = [r[-1] for r in rows if r[0] <= t]
        right = [r[-1] for r in rows if r[0] > t]
        # TODO: score = Gini hai phía có trọng số.
        score = (len(left) / len(rows)) * gini(left) + (len(right) / len(rows)) * gini(right)
        # TODO: nếu score tốt hơn thì cập nhật best_t,best_score.
        if score < best_score:
            best_score = score
            best_t = t
        #raise NotImplementedError("TODO: đánh giá ngưỡng " + str(t))
    return best_t, best_score

# Gini là hàm hỗ trợ; phần bạn viết là chọn ngưỡng.
# Sau TODO: (3.0, 0.0).
print(best_threshold(DATA))
