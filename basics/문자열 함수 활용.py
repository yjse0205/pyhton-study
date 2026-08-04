ss='Python is Easy.'"""
ss.upper() ##대문자로
ss.lower() ##소문자로
ss.swapcase() ##대소문자를 상호변환
ss.title() ##제일 앞글자만 대문자 변환


ss='파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
ss.count('공부')
print(ss.find('공부'), ss.rfind('공부'), ss.find('공부',5), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'), ss.index('공부',5))
print(ss.startswith('파이썬'), ss.startswith('파이썬',10), ss.endswith('^^'))

##find는 찾을 문자열이 몇번째에 위치하는지 뒤에 숫자는 시작위치 
##rfind는 함수를 오른쪽부터 센다 몇번째에 위치하는지
##find는 찾는게 없을때 -1 출력
##index는 find랑 동일
##startswith는 ('문자열')이게 그 위치에서 이 문자열로 시작하면 True아니면 False
##endswith는 그 문자열로 끝나면 True


ss=input("문자열 입력:  ")
print("출력 문자열:  ",end='') ##end=''이건 줄바꿈을 못하게 하는거임 

if ss.startswith('(')==False:  ##문자열의 시작이 '이 아니라면 ( <-- 출력
    print("(", end='')
    
print(ss,end='')

if ss.endswith(')')==False: ##문자열의 끝이 '이 아니라면 ) <--출력 
    print(")",end='')


ss='   파    이   썬   '
print(ss.strip())  ##앞 뒤 공백제거
print(ss.rstrip())  ##뒤쪽 공백제거
print(ss.lstrip()) ## 앞쪽 공백제거  다만 중간의 공백은 제거되지 않음



##중간의 공백을 제거하는 프로그램
inStr="   한글   Python   프로그래밍   "
outStr=""

for i in range(0,len(inStr)):
    if inStr[i]!=' ':    ## != 이거는 같지 않다라는 
        outStr+=inStr[i]  ##공백이 아닐때마다 outStr에 inStr[i]넣어

print("원 문자열==>"+'['+inStr+']')  ##각각의 문자열을 더하기 위해 +가 붙고 양옆에 대괄호 더해준거
print("공백제거 ==>"+'['+outStr+']')

##문자열의 변경 응용
ss.replace   ##얘가 문자열 변경
ss=input("문자열 입력==>")

print("출력 문자열==>",end='')
for i in range(0,len(ss)):
    if ss[i]!='o':
        print(ss[i],end='')
    else:
        print('$',end='')
"""
##split(), splitlines(), join()
##split 문자열을 공백이나 다른 문자로 분리해서 리스트를 반환
##splitlines 함수를 \n을 붙여도 행 단위로 정리
##join은 문자열을 합쳐줌 얘는 묶을 구분자를 ss='%'같이 정해줘야함
##center(숫자)는 숫자만큼이 전체 자릿수고 문자열은 가운데에 배치
##ljust는 왼쪽에, rjust는 오른쪽에 붙여서 출력
##zfill은 오른쪽으로 붙여쓰고 왼쪽 빈공간은 0으로 채움 
