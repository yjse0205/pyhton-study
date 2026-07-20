##조건문 if
a=int(input("랜덤 숫자:  "))

if a<100:
    print("100보다 작군요")
    print("거짓이므로 이 문장은 안보이겠죠?")

print("프로그램 끝")

##if else문은?
a=int(input("랜덤숫자: "))

if a<100:
    print("100보다 작군요")
else:
    print("100보다 크군요")
##if문 안에 if

a=175

if a>50:
    if a<100:
        print("50보다 크고 100보다 작다")
    else :
        print("100보다 크다")
else:
    print("50보다 작다")
      
