##while문은 조건식이 참일때 반복
i=0
while i<3:
    print("%d : while문" %i)
    i=1+i

i,hap = 0,0
i=1
while i<11:
    hap=hap+i
    i=i+1

print("1에서 부터 10까지의 합 %d" %hap)

##계산기? ch="" 이건 변수에 빈 문자열 넣는거
ch=""
a,b=0,0
while True:
    a=int(input("숫자입력: "))
    b=int(input("숫자입력: "))
    ch=input("연산자 입력: ")

    if(ch=="+"):
        print("%d+%d=%d입니다" %(a,b,a+b))
    elif(ch=="-"):
        print("%d-%d=%d입니다" %(a,b,a-b))
    elif(ch=="*"):
        print("%d*%d=%d입니다" %(a,b,a*b))
    elif(ch=="/"):
        print("%d/%d=%5.2f입니다" %(a,b,a/b))
    else:
        print("연산자 입력오류")
##break, continue
##break는 특정조건 입력해서 반복문 탈출
##continue는 특정조건 주어지면 그 조건 건너뛰고 진행되는 반복

hap,i=0,0

for i in range(1,101):
    hap+=i

    if hap>=1000:
        break

print("1~100의 합에서 최초로 1000이 넘는 위치: %d"%i)

##문자열의 한 글자씩 접근하기 위해선 str[0]이런식으로
##ch=numStr[i]이건 변수 ch에 문자열 numStr의  i번째 글자 입력된거
