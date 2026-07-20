
s1,s2,s3="100", "100.123", "9999999999999"
print(int(s1)+1,float(s2)+1,int(s3)+1)
##문자열로 구성되어있음
##int, float함수로 정수나 실수로 변환시켜줌

##변수 선언
money, c500, c100, c50, c10=0,0,0,0,0

##메인 코드
money=int(input("교환할 돈은 얼마?"))

c500=money//500
money%=500

c100=money//100
money%=100

c50=money//50
money%=50

c10=money//10
money%=10

print("\n오백원짜리==> %d 개 " % c500)
print("백원짜리==> %d개" % c100)
print("오십원짜리==>%d개" % c50)
print("십원짜리==>%d개" % c10)
print("바꾸지 못한 잔돈 ==> %d원" % money)
##기본적인 연산자 = + - * / //(얘는 몫) %(얘는 나머지값) **(얘는 제곱)
