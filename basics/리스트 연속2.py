parking=[]
top, carName, outCar=0, "A", ""
select=0

while(select!=3):
    select=int(input("<1> 자동차 넣기 <2>자동차 빼기 <3>끝 : "))

    if(select==1):
        if(top>=5):
            print("만차")
        else:
            parking.append(carName)
            print("%s 자동차 들어감. 주차장상태==>%s" %(parking[top],parking))
            top+=1
            carName=chr(ord(carName)+1)  ##carName이 A라면 B로 바꾸는거
    elif(select==2):
        if(top<=0):
            print("차 없음")
        else:
            outCar=parking.pop()
            print("%s 자동차 나감. 주차장 상태==>%s " %(outCar,parking))
            top-=1
            carName=chr(ord(carName)-1)
    elif(select==3):
        break;
    else:
        print("번호 없음")

print("현재 %d대 있음" %top)
           



print("현재 주차장에 %d 대 있음" %top)
        
## %s와 %d 갯수 일치 안했었음 if else elif 줄일
