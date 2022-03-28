import json
# 读
with open("a.json") as f:
    a = json.load(f)
print(a)

# 写
dic = {
    "name": "wangsan",
    "age": 19,
    "phone": "14500999900"
}
with open("b.json", 'w') as outfile:
    json.dump(dic,outfile)

