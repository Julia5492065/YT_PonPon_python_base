while True:
    data=input("請輸入數字: ")
    try:
        num=int(data)
        break
    except Exception:
        # num=0
        print("輸入格式錯誤，請重新再試!")
num=num*2
print(num)