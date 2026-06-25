import random

secret = random.randint(1, 100)
tries = 0

print("===== 猜數字遊戲 =====")
print("我已經想好一個 1 ~ 100 的數字了！")
print("每次猜錯，我會給你一個關於正確數字的四則運算提示。")
print("=========================")

while True:
    try:
        guess = int(input("請輸入你的猜測："))
    except ValueError:
        print("請輸入有效的整數！")
        continue

    tries += 1

    if guess == secret:
        print(f"恭喜！你猜對了！答案是 {secret}")
        print(f"你總共猜了 {tries} 次。")
        break

    op = random.randint(1, 4)

    if op == 1:
        n = random.randint(1, 50)
        result = secret + n
        print(f"[提示] 提示：正確數字 + {n} = {result}")
    elif op == 2:
        n = random.randint(1, max(secret - 1, 1))
        result = secret - n
        print(f"[提示] 提示：正確數字 - {n} = {result}")
    elif op == 3:
        n = random.randint(1, 10)
        result = secret * n
        print(f"[提示] 提示：正確數字 × {n} = {result}")
    else:
        divisors = [d for d in range(2, 11) if secret % d == 0]
        if divisors:
            n = random.choice(divisors)
            result = secret // n
            print(f"[提示] 提示：正確數字 ÷ {n} = {result}")
        else:
            n = random.randint(1, 10)
            result = secret * n
            print(f"[提示] 提示：正確數字 × {n} = {result}")

    print("再試一次吧！\n")
