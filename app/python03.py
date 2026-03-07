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
grade = 'B'
match grade:
    case 'A':
        print("A 탁월한 성적")
    case 'B':
        print("B 우수한 성적")
    case 'C':
        print("C 보통")
    case _:
        print("D 노력요함")

# match 뒤에 비교할 변수 작성.
# case 뒤에 해당 변수와 비교할 값. 
# 어떠한 case에도 일치하지 않을 경우 - case _ 
# _ : '그 외 모든 값' 와일드 카드 패턴 
# case _ : 이거는 생략 가능 
# 하나의 패턴을 하나의 case 에서 처리. 
# | 기호 사용 시, 여러 값 사용 가능 
grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case _:
        print("불합격입니다.")

# 조건부 표현식 
# 조건에 따라 변수에 서로 다른 값 대입 시, 사용
# 형태 : 
# 변수 = 참일때값 if 조건 else 거짓일때 값
score = 85
result = '합격' if score >= 60 else "불합격"
print("result ? " + result)

# while문 
# while 조건문:
#     수행할문장1
#     수행할문장2
#     수행할문장3
# while 조건문이 참인 동안 while 문에 속한 문장 반복 수행.
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    # treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# treeHit = treeHit + 1
# treeHit += 1

# ctrl + shift + / 버튼 누르면 """ """ 가능 
# number가 4가 아닌동안 계속 prompt 출력.
# number = int(input()) : 사용자 숫자 입력을 받아들이는 것.
# int, input 함수는 내장 함수에서 다룸. 
prompt = """ 
    1. Add
    2. Del
    3. List
    4. Quit
 """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while 문 강제로 빠져나가기. (break)
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 커피 10 잔을 다 판매할 떄 까지 해당  while 문 진행. 
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# while 문의 맨 처음으로 돌아가기. (continue)
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
# continue 시, while 문의 첫번쨰인 "a = a + 1" 실행. 

# while-else 문
# while 문이 정상적으로 종료되었을 때(break로 빠져나가지 않았을 때) else 절이 실행된다.
# break 문으로 while 문을 빠져나가면 else 절은 실행되지 않는다.
count = 0
while count < 3:
    print(f"카운트: {count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

# 무한 루프.
# while True: 
#     수행할_문장1 
#     수행할_문장2
# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# for 문의 기본 구조. 
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2

test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print("i ? " + i);

# a 리스트 요솟값이 튜플이라 자동으로 각각의 요소가 first 와 last 변수에 대입 됨. 
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number + 1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

# for 문과 continue
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number + 1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# for 문과 함께 쓰는 range 함수. 
# 숫자 리스트를 자동으로 만들어 주는 함수.
a = range(10)
# 0 부터 10 "미민"의 숫자를 포함하는 range 객체.
a = range(1, 11)
# 처음과 마지막 숫자를 지정하면, 마지막 숫자(11)은 포함되지 않는다. 
add = 0 
for i in range(1, 11): 
    add = add + i 
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for와 range를 이용한 구구단
# 4줄 만으로 구구단 가능. 
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ") 
    print('') 

# print 문의 end 매개변수에는 줄바꿈 문자(\n)가 기본값으로 설정

# 리스트 컴프리헨션(list comprehension)
# 문법 : [표현식 for 항목 in 반복_가능_객체 if 조건문]
# [표현식 for 항목1 in 반복_가능_객체1 if 조건문1
    #   for 항목2 in 반복_가능_객체2 if 조건문2
    #   ...
    #   for 항목n in 반복_가능_객체n if 조건문n]
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

# a 리스트의 각 항목에 3을 곱한 결과
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

# 리스트 중 짝수에만 3을 곱한 결과
a = [1,2,3,4]
result = [num * 3 for num in a if num%2 ==0]
print(result)

result = [x*y for x in range(2,10)
            for y in range(1,10)]
print(result)

# for - else 문 
# for 문이 정상적으로 종료 시(break로 빠져나가지 않을 시에), else 절 실행.

for i in range(5):
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

for i in range(5):
    if i == 3:
        break;
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# enumerate 함수 사용. 
# 리스트의 순서(인덱스)와 값을 함께 구하고 싶을 때
# 0부터 시작하는 인덱스 번호 자동 생성 가능. 
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, 1):  # 1부터 시작
    print(f"{i}: {fruit}")

# zip 함수. 
# 두개 이상의 리스트 동시 순회. 
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")