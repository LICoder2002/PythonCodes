def get_age(n):
    if n == 1:
        return 10
    else:
        return get_age(n-1) + 2

# 测试
n = int(input("请输入年龄n："))

print(get_age(n))
