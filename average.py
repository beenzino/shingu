import random

n=1
while(n==1):
    cla = int(input("교과목 개수를 입력하세요(5개까지 가능): "))
    if cla>5:
        print("개수를 다시 입력하세요(최대 5개)")
    elif cla==0:
        print("최소 1개 이상 입력하세요")
    elif cla==1:
        print("1초과 5이하의 숫자를 입력하세요")
    else:
        break
if cla==1:
    a=[0]
    guk=[random.randint(0,100)]
    score=[guk]
elif cla==2:
    a=[0,0]
    guk=[random.randint(0,100),random.randint(0,100)]
    su=[random.randint(0,100),random.randint(0,100)]
    score=[guk,su]
elif cla==3:
    a=[0,0,0]
    guk=[random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    su=[random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    yeong=[random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    score=[guk,su,yeong]
elif cla==4:
    a=[0,0,0,0]
    guk=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    su=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    yeong=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    kwa=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    score=[guk,su,yeong,kwa]
elif cla==5:
    a=[0,0,0,0,0]
    guk=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    su=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    yeong=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    kwa=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    sa=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    score=[guk,su,yeong,kwa,sa]

b=0
for i in score:
    for n in i:
        a[b]+=n
        b+=1
    b=0
if cla==2:
    z, x= a
    aver = [z/2,x/2]
    print(aver)
elif cla==3:
    z, x, c= a
    aver = [z/3,x/3,c/3]
    print(aver)
elif cla==4:
    z, x, c, v= a
    aver = [z/4,x/4,c/4,v/4]
    print(aver)
elif cla==5:
    z, x, c, v, n= a
    aver = [z/5,x/5,c/5,v/5,n/5]
    print(aver)
    



