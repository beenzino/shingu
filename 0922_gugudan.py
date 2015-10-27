print ("구구단 몇단을 계산할까요?")
dan = int(input())

print ("구구단 " + dan + "단을 계산합니다.")
for i in range(1,9):
    print (dan+"x"+i+"="+dan*i)
