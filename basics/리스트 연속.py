#리스트의 생성과 초기화
"""aa=[]
bb=[]
value=0

for i in range(0,100):
    aa.append(value)
    value+=2

for i in range(0,100):
    bb.append(aa[99-i])

print("bb[0]은 %d, bb[99]는 %d입력됨" %(bb[0], bb[99]))
          

##리스트 역순
aa=[10,20,30,40]
print("aa[-1] %d, aa[-2] %d" %(aa[-1],aa[-2]))

##리스트 범위지정
aa=[10,20,30,40]
aa[0:3]
aa[2:4]

##리스트 연산
aa=[10,20,30]
bb=[40,50,60]
print(aa+bb)
print(aa*3)


##리스트 바꾸기,추가,제거
aa=[10,20,30]
aa[1]=200
print(aa)
aa[1:2]=[200,201] ##얘는 이제 리스트의 1번 2번자리에 추가되는
print(aa)
del(aa[1]) ##얘는 리스트에서 1번 제
print(aa)
aa[1:2]=[] ##얘는 리스트에서 1번부터 2번을 제거
print(aa)
"""
##리스트 조작함수
myList=[30,10,20]
print("현재 리스트 : %s " %myList)

myList.append(40)
print("리스트에 40 추가 %s" %myList)

print("리스트의 제일 뒤의 항목 빼내고 삭제 %s" %myList.pop())
print("현재 리스트: %s" %myList)

myList.sort()
print("리스트의 항목 정렬: %s " %myList)

myList.reverse()
print("리스트 역순으로 : %s" %myList)

myList.insert(2,222)
print("지정된 자리에 리스트값 삽입: %s" %myList)

myList.remove(222)
print("리스트에서 지정된 값 제거: %s " %myList)

myList.extend([77,88,77])
print("리스트 뒤에 리스트 추가: %s" %myList)

print("지정된 값의 갯수: %d" %myList.count(77))
