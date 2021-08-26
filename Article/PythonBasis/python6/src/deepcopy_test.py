from copy import deepcopy

d = {}

d["names"] = ["Alfred", "Bertrand"]

b = d.copy()

b["names"] = "bob"

# 字典数据类型的copy函数,当简单的值替换的时候，原始字典和复制过来的字典之间互不影响

# print("#字典数据类型的copy函数,当简单的值替换的时候，原始字典和复制过来的字典之间互不影响")
#
# print(b)
#
# print(d)

c = d.copy()

dc = deepcopy(d)

# 字典数据类型的copy函数，但是当添加，删除等修改操作的时候，两者之间会相互影响。

print("#字典数据类型的copy函数，但是当添加，删除等修改操作的时候，两者之间会相互影响。")

d["names"].append("Clive")

print(d)

print(c)
print(dc)