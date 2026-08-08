"""
파일 입출력
read(), readline(), readlines()
write(), writelines()
읽기용 : 변수명=open("파일명","r")
쓰기용 : 변수명=open("파일명","r")
r:읽기 w:쓰기, r+:읽기+쓰기, a:쓰기 기존파일 있을시 이어쓰기, t:텍스트모드
b:바이너리 모드

inFp=None  ##변수에아무것도 없다
inStr=""   ##변수에 빈 문자열 입력

inFp=open("c:/temp/data1.txt","r", encoding="utf-8") ##inFp변수에 파일 읽기모드로
##UFT-8 방식으로 읽겠다.

inStr=inFp.readline() ##파일에서 한 줄을 읽는함수 readline으로 가져오면 \n기본 포함
print(inStr,end="") ##이게 print에서 추가로 붙는 \n을 지움

inStr=inFp.readline()
print(inStr,end="")

inFp.close()

##한번에 모두 읽기

inFp=None
inList=""

inFp=open("C:/temp/data1.txt", "r", encoding='utf-8')

inList=inFp.readlines()
print(inList)

inFp.close()
##readlines()는 각 행을 리스트의 항목으로 저장해서 한번에 반환함 줄바꿈 안됨
##줄바꿈을 하기위해 리스트 처리방식 사용

inFp=None
inList,inStr=[],""

inFp=open("C:/temp/data1.txt","r", encoding='utf-8')

inList=inFp.readlines() ##inList에서 inStr로 차례대로 하나씩 옮겨지는 과정
for inStr in inList:
    print(inStr,end="")

inFp.close

##type명령어 지정한 파일의 내용을 화면에 출력하는기능
inFp=None
fName, inList, inStr="",[],""

fName=input("파일명을 입력하세요: ")
inFp=open(fName, "r", encoding='utf-8')

inList=inFp.readlines()
for inStr in inList:
    print(inStr,end="")

inFp.close()

##출력결과를 파일에 저장하는 방식
outFp=None
outStr=""

outFp=open("c:/temp/data2.txt","w", encoding='utf-8')
##얘는 outFp에 파일쓰기모드로 열어버림
while True:    ##동작되는동안 outStr에 입력되고 입력이 되는동안 if문 반복됨
    outStr=input("내용 입력: ")
    if outStr !="":
        outFp.writelines(outStr+"\n")  ##문자열 여러개를 한번에 쓰는거고 \n을 포함하지 않기에 수동으로 넣어줌
    else:
        break

outFp.close()
print("---정상적으로 파일에 써졌음---")

##copy구현
inFp,outFp=None,None
inStr=""

inFp=open("c:/windows/win.ini","r",encoding='utf-8')
outFp=open("c:/temp/data3.txt","w",encoding='utf-8')

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("정상적으로 파일이 복사되었음")
"""     
