import turtle

# 创建一个Turtle对象
t = turtle.Turtle()

# 绘制等边三角形
for i in range(3):
    t.forward(100)
    t.left(120)

# 关闭窗口
turtle.done()
