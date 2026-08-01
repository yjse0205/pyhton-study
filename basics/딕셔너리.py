dic1={1:'a', 2:'b', 3:'c'}
print(dic1)

student1={'학번':1000, '이름':'홍길동', '학과':'열공학과'} ##문자열 '넣는거
print(student1)

student1['연락처']='010-4715-1246' ##없는경우 추가가됨
print(student1)

student1['학과']='파이썬학과' ##얘는 추가가 아니라 값이 변경됨
print(student1)

del(student1['연락처']) ##삭제도 가능
print(student1)

print(student1['학번']) ##이런식으로 각각 접근가능

print(student1.keys()) ##전체를 나타냄  이건 딕셔너리의 모든 키를 반환한다.

print(student1)

print(student1.values()) ##딕셔너리의 값을 반
