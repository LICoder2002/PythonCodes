n = int(input("请输入整数n："))

sum = 0
for i in range(1, n+1):
    sum += i

print("1到{}之间所有整数的和为：{}".format(n, sum))
