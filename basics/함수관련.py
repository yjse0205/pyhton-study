"""
coffee=0  ##변수만듬 p249의 코드

def coffee_machine(button):  ##coffee-machine 함수설정 input으로 선택한 번호를
    ##button에 받음
    print()
    print("#1. 뜨거운 물 준비됨.")
    print("#2. 종이컵 준비됨.")

    if button==1:
        print("#3. 보통커피를 탄다.")
    elif button==2:
        print("#3. 믹스커피를 탄다.")
    elif button==3:
        print("#3. 블랙커피를 탄다.")
    else :
        print("#3. 아무거나 탄다.")

    print("#4. 물을 붓는다.")
    print("#5. 스푼으로 저어서 녹인다.")
    print()



coffee=int(input("어떤 커피 드릴까요? (1:보통. 2:설탕, 3:블랙) ")) ##선택한 번호가 coffee로
coffee_machine(coffee) ##사용자가 입력한 coffee값을 함수에 전달하게됨 
print("커피 나왔습니다.")

def plus(v1,v2):
    result=0
    result=v1+v2
    return result

hap=0
hap=plus(100,200)  ##여기서 함수 동작시킴 
print("100과 200의 plus()함수 결과는 %d." %hap)


##계산기 함수?
def calc(v1,v2,op):
    result=0
    if op=='+':
        result=v1+v2
    elif op=='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    elif op=='/':
        result=v1/v2

    return result

res=0
var1,var2,oper=0,0,""

oper=input("연산자 입력: ")
var1=int(input("첫번째 숫자 입력: "))
var2=int(input("두번째 숫자 입력: "))

res=calc(var1,var2,oper)
print("계산기 : %d %s %d= %d" %(var1,oper,var2,res))


##지역변수 전역변수 Local, Global

def func1():
    a=10  ##이게 지역변수
    print("func1()에서 a의 값 %d"%a)

def func2():
    print("func2()에서 a의 값 %d"%a)

a=20  ##이게 전역변수

func1()
func2()

##함수의 반환값과 매개변수
def func1():
    result=100
    return result  ##이게 반환값

def func2():
    print("반환값 없는 함수 실행") ##얘가 반환값 없는 함수 

hap=0
hap=func1()
print("func1()에서 돌려준 값==>%d" %hap)
func2()

##매개변수
def para2_func(v1,v2):   ##매개변수 v1,v2 2개
    result=0
    result=v1+v2
    return result

def para3_func(v1,v2,v3):  ##매개변수 v1,v2,v3 3개 
    result=0
    result=v1+v2+v3
    return result

hap=0
hap=para2_func(10,20)
print("매개변수 2개 함수 호출 결과==>%d"%hap)
hap=para3_func(10,20,30)
print("매개변수 3개 함수 호출 결과==>%d"%hap)

##매개변수 개수 지정 안해두는법

def para_func(*para):   ##매개변수 이름앞에 *붙여주면 매개변수가 튜플형식으로
    result=0
    for num in para:
        result=result+num

    return result

hap=0

hap=para_func(10,20) ##여기서 para에 (10,20) 들어가게 된거임
print("매개변수 2개 함수 호출 결과==>%d" %hap)
hap=para_func(10,20,30)
print("매개변수 3개 함수 호출 결과==>%d" %hap)

    
##로또복권번호 추첨 프로그램
import random

def getNumber():
    return random.randrange(1,46)  ##randrange(시작,끝+1) 시작~끝까지의 숫자중 랜덤1개

lotto=[]
num=0

print("**로또 추첨을 시작합니다.**")

while True:
    num=getNumber()

    if lotto.count(num)==0:   ##lotto리스트 안에 num이 몇개있냐 0개면 아래 실행
        lotto.append(num)

    if len(lotto)>=6:
        break

print("추첨된 로또 번호==> ",end='')
lotto.sort()  ##얘는 그냥 작은숫자부터 정렬시킬려고 하는거임 
for i in range(0,6):
    print("%d " %lotto[i],end='')
"""
##모듈==함수의 집합
def func1():
    print("Func.py의 func1()이 호출됨.")

def func2():
    print("Func.py의 func2()가 호출됨.")

def func3():
    print("Func.py의 func3()가 호출됨.")
##여기까지가 함수 설정한 파일
import Func
Func.func1()
Func.func2()
Func.func3()
##여기까지가 다른파일에서 설정된 함수 호출한 
