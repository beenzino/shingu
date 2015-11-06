c=0
while(c==0):
    import random
    a = ["0","0","0"]
    a[0] = str(random.randint(1,9))
    a[1] = a[0]
    a[2] = a[0]
    while(a[0]==a[1]):
        a[1] = str(random.randint(1,9))
    while(a[1]==a[2] or a[0]==a[2]):
        a[2] = str(random.randint(1,9))
    print("야구 게임을 시작합니다, 0을 입력하시면 언제든지 종료 가능합니다")

    strike=0
    count = 0
    while(strike<3):
        ab = str(input("3자리 숫자를 입력하세요: "))
        if ab == str(0):
            count=0
            break
        elif(len(ab)!=3):
            print("3자리로 입력하세요")
            continue
        elif(ab[0]==ab[1] or ab[1]==ab[2] or ab[0]==ab[2]):
            print("숫자는 중복되서는 안 됩니다")
            continue
        '''elif(ab.isdigit()==False):
            print("문자를 입력하면 혼납니다")
            continue'''
        else:
            strike=0
            ball=0
            for i in range(0,3):
                for j in range(0,3):
                    if(ab[i]==str(a[j]) and i==j):
                        strike +=1
                    elif(ab[i]==str(a[j]) and i!=j):
                        ball +=1
            print("Strike : ",strike," Ball : ",ball)
            count +=1
    if count == 0:
        print("게임을 종료합니다")
    else:
        print(count,"번 만에 맞추셨습니다")
        d=0
        while(d==0):
            abc = input("게임을 한 번더 하시겠습니까? YES/NO: ")
            abc2 = abc.lower()
            if abc2 == "yes":
                print("다시 시작됩니다")
                d=1
            elif abc2 == "no":
                print("게임을 종료합니다")
                d=1
                c=1
            else:
                print("YES/NO로 입력해주시기바랍니다")
    


