# 載入turtle模組
import turtle as tu

# 顯示畫布
tu.showturtle()

# 畫正多邊形
tu.setheading(180)
tu.color('green')
tu.pendown()
tu.begin_fill()
tu.circle(50, 360, 6)  # 邊長、內角和、幾邊形
tu.end_fill()
tu.color('red')