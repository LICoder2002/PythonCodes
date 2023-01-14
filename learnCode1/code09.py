# 关系运算符

# 数字比较大小
# a = 10
# b = 12

# 字符串比较大小——字典顺序
a = 'hello'
b = 'world'

print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

# 浮点数比较大小
print(1.0 + 2.0 == 3.0)  # True
print(0.1 + 0.2 == 0.3)  # False

print(0.1)
print(0.2)
print(0.1 + 0.2)  # 0.30000000000000004
print(0.3)


a = 0.1 + 0.2
b = 0.3
# 判断a - b 是否在误差范围之内
print(-0.000001 < (a - b) < 0.000001)  # python中支持连续比较
