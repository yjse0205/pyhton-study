
for i in range(0,3,1):
    print("for문 공부")
##for 변수 i range(시작, 끝+1, 증가값)


##print문의 끝에 end=""
for i in range(1,6,1):
    print("%d " %i,end="")

##뭐 변수 설정해서 for문 사용
i,hap=0,0

for i in range(1,11,1):
    hap=i+hap
    
print("\n1에서 10까지의 합: %d" %hap)

##내가 시작,끝,증가값 설정하는 for문

i, hap=0, 0
num1,num2,num3=0,0,0

num1=int(input("시작값 입력: "))
num2=int(input("끝값 입력: "))
num3=int(input("증가값 입력: "))

for i in range(num1,num2+1,num3):
    hap=i+hap

print("%d에서 %d까지 %d씩 증가한 값의 합: %d" %(num1,num2,num3,hap))

##for문 안의 for 바깥for문*안쪽for문
i,k=0,0
for i in range(0,3,1):
    for k in range(0,2,1):
        print("반복횟수 (i값: %d, k값: %d)" %(i, k))
