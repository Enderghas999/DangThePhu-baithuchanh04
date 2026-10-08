# Dữ liệu nhỏ để đọc và đối chiếu cây:
DATA = [["mây", "nhẹ", "có"], ["mây", "mạnh", "có"],
        ["nắng", "nhẹ", "có"], ["nắng", "mạnh", "không"]]
TREE = (0, {"mây": "có",
            "nắng": (1, {"nhẹ": "có", "mạnh": "không"})})

def predict(tree, sample):
    current = tree
    while not isinstance(current, str):
        col, branches = current
        value = sample[col]
        if value not in branches:
            raise ValueError("Thuộc tính chưa gặp: " + value)
        # TODO: current nhận cây con branches[value].
        current = branches[value]
        #raise NotImplementedError("TODO: đi theo một cạnh")
    return current

# Sau TODO: kết quả "không", rồi "có".
print(predict(TREE, ["nắng", "mạnh"]))
print(predict(TREE, ["mây", "nhẹ"]))
