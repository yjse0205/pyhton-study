"""바이너리 파일은 비트로 단위가 이루어진 파일 txt를 제외한 거의 모든파일"""
##메모장 실행파일 복사, txt파일이 아니라 encoding 불필요 r>rb w>wb
"""
inFp, outFp=None, None
inSTr=""

inFp=open("c:/Windows/notepad.exe","rb")
outFp=open("c:/temp/notepad.exe","wb")  ##없는파일을 쓰기모드로 열었음

while True:
    inStr=inFp.read()
    if not inStr:  ##더이상 읽을 내용 없을시에 이게 참이됨
        break
    outFp.write(inStr)  ##읽은 내용이 outFp로 새 파일에 

inFp.close()
outFp.close()
print("바이너리 파일 복사됨")
"""
