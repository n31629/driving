i = 0
while True:
    if i < 3 :
        password = input('請輸入密碼：')
        if password == 'a123456':
            print('登入成功')
            break
        elif password != 'a123456' :
                i = i + 1
                print('密碼錯誤，還剩下',3-i,'次機會')
    else:
        print('密碼輸入錯誤已達上限，請15分鐘後登入')
        break