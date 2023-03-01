import turtle

# 创建一个Turtle对象，用于绘制图形
t = turtle.Turtle()

# 设置画布的背景色为白色
turtle.bgcolor("white")

# 设置画笔的颜色为红色
t.color("red")

# 开始绘制三角形
t.begin_fill()
for i in range(3):
    t.forward(100)  # 向前移动100像素
    t.right(120)  # 右转120度，绘制等边三角形
t.end_fill()

# 隐藏画笔
t.hideturtle()

# 点击关闭窗口退出程序
turtle.exitonclick()
