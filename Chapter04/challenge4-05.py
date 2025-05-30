def god(a):
    try:
        a = int(input())
        print("入力された文字=",a)
        print("入力された文字を小数点化した結果=",float(a))
        return a
    except ValueError:
        print("整数、または、小数点数を入力してください。")
#a = str(4)
#a = str("あ")
a = str("")
god(a)
