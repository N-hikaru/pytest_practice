# 数値の比較
x_sum = 2
assert x_sum == 2, "1+1は2です"
print("数値チェックOK")

# 文字列の比較
hello = "hello" + " " + "world"
assert hello == "hello world", "文字列の結合が間違っています"
print("文字列のチェックOK")

# リストの比較
items = []
items.append("python")
assert items == ["python"], "アイテムが間違っています"
print("リストチェックOK")
