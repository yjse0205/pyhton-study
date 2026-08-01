##리스트
a,b,c,d=0,0,0,0
hap=0

a=int(input("1번째 숫자: "))
b=int(input("2번째 숫자: "))
c=int(input("3번째 숫자: "))
d=int(input("4번째 숫자: "))

hap=a+b+c+d

print("합계: %d" %hap)
##이 상태에서 리스트 만들고 넣기

aa=[0,0,0,0]
hap=0

aa[0]=int(input("1번째 숫자: "))
aa[1]=int(input("2번째 숫자: "))
aa[2]=int(input("3번째 숫자: "))
aa[3]=int(input("4번째 숫자: "))

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계= %d"%hap)

##for과 같이 사용

aa=[]
for i in range(0,4) :
    aa.append(0)    ##얘가 리스트 이름 정하고 0부터 3번까지 리스트 만듬 0 으로
hap=0

for i in range(0,4) :
    aa[i]=int(input(str(i+1)+" 번째 숫자: "))  ##얘가 출력되면 1번째 숫자: 입력 이런식으로 반복

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계: %d" %hap) 

