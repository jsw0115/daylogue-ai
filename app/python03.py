## 집합 자료형 
# 집합 자료형 : set 함수. 
# 리스트 입력 혹은 문자열 입력하여 자료형 설정 가능
s1 = set([1, 2, 3])
print("s1 : " + str(s1))
s2 = set("Hello")
print("s2 : " + str(s2))
# 비어있는 자료형
# set()
s3 = set()
print("s3 : " + str(s3))
s4 = {1,2,3,4}
print("s4 : " + str(s4))
# (주의) s= {} 형태는 딕셔너리 형태

# 집합 자료형 특징
# 1. 중복 허용 안함.
# 2. 순서 없음  → 인덱싱으로 요솟값을 얻을 수 없음. 
# ☞ 인덱싱으로 접근하려면 리스트, 튜플로 변환 후 사용해야함. 
# 데이터 중복 제거하는 필터로 사용. 
s1 = set([1, 2, 3])
l1 = list(s1)
print("set → s1 : " + str(s1))
print("list → l1 : " + str(l1))
t1 = tuple(s1)
print("tuple → t1 : " + str(t1))

# 합집합 & 차집합 & 교집합. 
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 
s1 & s2
s1.intersection(s2)

# 합집합
s1 | s2
s1.union(s2)

# 차집합
s1 - s2
s1.difference(s2)
# {1, 2, 3}

s2 - s1
s2.difference(s1)
# {8, 9, 7}

# 값 1개 추가 - add

# 값 여러개 추가 - update
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1
# {1, 2, 3, 4, 5, 6}

# 특정 값 제거 - remove
# 없는 값을 제거하려하면 오류 !!! 

# 특정 값 제거 - discard 
# 없는 값이어도 오류 안남 !! 

# 모든 값 제거. 
# 결과는 set()

# ★ 자료형의 참과 거짓 ★
# 참(True) : 
#   문자열, 리스트, 튜플, 딕셔너리 : 값이 있을 경우
# 거짓(False) : 
#   문자열, 리스트, 튜플, 딕셔너리 : 값이 비어 있을 경우
#   숫자 : 값이 0일 때 거짓
#   None 일 경우. (값이 없음을 나타내는 객체.)

# 파이썬 예약어 모음. 
# 예약어는 변수로 사용 불가. 
# False, None, True, and, as, assert, break, class, continue, def, 
# del, elif, else, except, finally, for, from, global, if, import, 
# in, is, lambda, nonlocal, not, or, pass, raise, return, try, 
# while, with, yield

# 자료형 복사. 
a = [1,2,3]
b = a
id(a)
id(b)
a is b
a[1] = 4
# b도 같이 수정됨. 

# 1. [:] 이용.
a=[1,2,3]
b=a[:]
a[1] = 4

# 2. copy 이용
from copy import copy
a = [1,2,3]
b = copy(a)     # 또는 b = a.copy()
b is a
# copy를 하게 되면 변수 값은 같지만 "서로 다른 객체"
# 따라서 b is a 는 False 리턴

# 변수를 만드는 방법 
# 1. 영문자, 숫자, 언더스코어(_)만 사용할 수 있다.
# 2. 숫자로 시작할 수 없다.
# 3. 예약어는 사용할 수 없다.
# 4. 대소문자를 구분한다.

# 튜플로 대입
a, b = ('python', 'life')
(a, b) = 'python', 'life'
# 리스트로 대입 
[a, b] = ['python', 'life']

# 변수에 같은 값 대입. 
a = b = 'python'

# 두 변수의 값 변경하기. 
a = 3
b = 5
a,b = b,a

# 제어문 
# IDLE 셸 주의 사항 !! 
# >>> 이러한 예제는 파이썬 셸에서 실행 필요.
# IDLE에서는 줄바꿈 표시(...) 보이지 않아 오류 확률이 높아짐.
# 방법 
# if 조건문:
#     수행할_문장1
#     수행할_문장2
#     수행할_문장3
# # 오류 발생 1 
# if 조건문:
#     수행할_문장1
# 수행할_문장2
#     수행할_문장3
# !!! 들여쓰기는 항상 같은 깊이로!! 

#  들여쓰기를 할 때 공백 문자 4개를 사용하는 것을 권장
# 조건문 다음에 콜론(:)을 잊지 말자!
# if, while, for, def, class 모두 콜론(:)이 들어감.
# 콜론을 사용해 들여쓰기를 하기에 파이썬에서는 들여쓰기로 해결. 

# and. or. not
# not x : x가 거짓이면 참이다. 
money = 2000
card = True
if not money > 2000:
    print("걸어가기")
else:
    print("택시 타기기")

# in, not in
# x in 리스트 
# x not in 리스트
# x in 튜플
# x not in 튜플
# x in 문자열 
# x not in 문자열 
1 in [1, 2, 3]
1 not in [1, 2, 3]
'a' in ('a', 'b', 'c')
'j' not in 'python'

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# pass
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드 꺼내")

# pass 가 실행되고 아무일도 일어나지 않음. 

# elif 
# else if 문과 같은거.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else: 
    print("걸어가")

# match-case 문 
# 파이썬 3.10 버전부터 사용 가능. 
# if - elif - else 문으로 조건 판단하는 대신, 하나의 변수 값에 분기하는 코드를 줄일 수 있음.
