# 逻辑运算符

a = 10
b = 20
c = 30
# print((a < b) and (b < c))
# print(a < b and b > c)
# print(a > b or b > c)
# print(a < b or b > c)
# print(not a < b)
# print(not a > b)

print(a > b and 10 / 0 == 1)  # and左边为假，整体为假，右边不计算
print(a < b or 10 / 0 == 1)   # or左边为真，整体为真，右边不计算
