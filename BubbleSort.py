a=0
while(a==0):
    b = int(input("리스트크기를 입력하세요: "))
    if(b!=0):
        list=[]
        c=b+1
        for size in range(1,c):   
            list.append(size)
            import random
            random.shuffle(list)
        print ("입력한 리스트: ",list)
        d=len(list)
        count=0
        for i in range(d):
            for j in range(0,len(list)):
                if (list[i]<list[j]):
                    list[i],list[j]=list[j],list[i]
                    count+=1
        print("버블소트: ",list)
        print("바뀐횟수: ",count)
    else:
        break
print("THE END")
