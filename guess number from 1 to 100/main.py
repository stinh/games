import random
import info

# 歡迎畫面，規則解說
print(info.intro)
input()

# 產生答案1~100，用變數lower_limit和upper_limit來存上下限值
ans = random.randint(1, 100)
lower_limit = 1
upper_limit = 100

# TODO: 設計防呆機制，先用一個函式簡單代表，簡單把輸入的str轉換成int
def check_input(user_input):
    return int(user_input)


while True:
    # 讓user猜數字
    guess_str = input(f"猜一個{lower_limit}~{upper_limit}之間的數字：")

    # 呼叫函示把輸入轉換成數字
    guess = check_input(guess_str)

    # 判定：根據太大或太小改變範圍

    if guess == ans:
        print("答對了！")
        # 下面這行耍花俏而已XD
        print(info.bingo)
        # 猜對了就跳出loop
        break
    elif guess > ans:
        upper_limit = guess
    else:
        lower_limit = guess
    print("猜錯囉！縮小範圍再猜一次")
    # Loop回去重複猜