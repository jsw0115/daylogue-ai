# 파이썬 함수.
""" 
    def 함수_이름(매개변수):
        수행할_문장1
        수행할_문장2
        ...
"""

# def 함수 만들 떄 사용하는 예약어. 
# 함수 이름 뒤 괄호 안의 매개변수
# 함수에서 수행할 문장 입력.
def add (a, b):
    return a + b;

a = 3
b = 4
c = add(a,b)
print("add 함수 : ", c)

# 입력값 없는 함수. 
def say():
    return "HI"

a = say()
print(a)

# 반환값 없는 함수.
def add(a, b):
    print("%d, %d의 합은 %d." % (a, b, a+b))

add(1,2)

# 입력값, 반환값 없는 함수. 
def say():
    print('Hi')

say()

# 매개변수 지정하여 호출.
def sub(a, b):
    return a-b

result = sub(a=2, b=3)
print("result : ", result)

# 입력 값 개수를 확실히 모를 때
""" 
    def 함수_이름(*매개변수):
        수행할_문장
        ...
"""

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print("add_many(1,2,3) : ", result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print("add_many(1,2,3,4,5,6,7,8,9,10) : ", result)

def add_mul(choice, *args): 
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
         result = 0 
         for i in args: 
             result = result + i 
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
         result = 1 
         for i in args: 
             result = result * i 
    return result 

result = add_mul('add', 1,2,3,4,5)
print("result : ", result)


result = add_mul('mul', 1,2,3,4,5)
print("result : ", result)

# 키워드 매개변수, kwargs
# 키워드 매개변수란.
#   "키워드 = 값" 형태로 전달하는 매개변수를 받을 때 사용.
# 사용 시, 별 2개(**) 를 붙여 사용. 
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
print_kwargs(name='홍길동', age=25, city='서울', job='개발자')

def create_profile(**info):
    print("=== 프로필 정보 ===")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이=30, 직업='프로그래머', 취미='독서')

def mixed_function(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수들: {kwargs}")

mixed_function('홍길동', 1, 2, 3, age=25, city='서울')

# kwargs는 'keyword arguments'의 약자이며 args와 마찬가지로 관례적으로 사용

# 함수의 반환 값은 언제나 하나! 
def add_and_mul(a,b): 
    return a+b, a*b

# add_and_mul 함수의 반환값 a+b와 a*b는 "튜플값" 하나인 (a+b, a*b)로 반환
result = add_and_mul(3,4)
print("result : ", result)

# 하나의 튜플 값을 2개의 값으로 분리하는 방법
result1, result2 = add_and_mul(3, 4)
print("result1 : ", result1, ", result2 : ", result2)

def add_and_mul(a,b): 
    return a+b 
    return a*b 

# 두 번째 return 문인 return a * b는 실행되지 않음.

# return 쓰임새 2 
# 함수를 그냥 빠져나가고 싶을 떄 단독으로 return 
# 예제 1. 
def say_nick(nick): 
    if nick == "바보": 
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('바보')

# 매개변수 man에 미리 값을 넣어줌.
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)

# 함수 매개변수에 초기 값 설정 시, 주의사항.
""" 
# Non-default argument follows default argument
# 초깃값이 없는 매개변수(age)는 초깃값이 있는 매개변수(man) 뒤에 사용할 수 없다
def say_myself(name, man=True, age): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")
"""

# 함수 안에서 선언한 변수의 효력 범위
# 함수 밖에서도 동일하게 사용한다면 어떻게 될지.
# a = 1
# def vartest(a):
#     a = a +1

# vartest(a)
# print(a)
# 함수 안에서 사용하는 매개변수는 함수 안에서만 사용하는 '함수만의 변수'
# def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관없다

def vartest(x):
    x = x + 1

vartest(3)
# name 'x' is not defined 
# 변수는 어디에도 선언되지 않았기 때문
# print(x)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용. 
a = 1 
def vartest(a): 
    a = a +1 
    return a

# vartest 함수의 반환값이 대입
# 함수 안의 a 매개변수는 함수 밖의 a와는 다름.
a = vartest(a) 
print(a)

# 2. global 명령어 사용.
a = 1 
def vartest(): 
    # global : 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻
    # !! but, global 명령어는 사용하지 않는 것이 좋음
    # 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니기 때문 !! 
    global a 
    a = a+1

vartest() 
print(a)

# 리스트나 딕셔너리는 함수에서 변경 가능하다
# "숫자"나 "문자열" 값은 함수 안에서 변경해도 함수 밖의 원래 값에는 영향을 주지 않지만, 
# "리스트"나 "딕셔너리"는 "변경 가능한" 자료형이다.
# 함수 안에서 값을 변경하면 원래 딕셔너리도 함께 변경
# 원본이 변경될 수 있다는 점을 기억
def change_list(my_list):
    my_list.append(4)  # 리스트에 값을 추가

a = [1, 2, 3]
change_list(a)
print(a)

# lambda 예약어
# 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할
# 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰임.
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식

add = lambda a, b: a+b
result = add(3, 4)
print(result)

# lambda로 만든 함수는 return 명령어가 없어도 표현식의 결괏값을 반환

# 함수의 독스트링(Docstring)
# 함수에 대한 설명을 문서화하는 방법
""" 

 """

# 사용자 입출력.
# 사용자가 입력한 값을 변수에 대입하고 싶을 때
# input : 사용자가 키보드로 입력한 모든 것을 문자열로 저장
a = input()
print("Input a : ", a)

# 프롬프트 띄워 사용자 입력 받기. 
# input()의 괄호 안에 안내 문구를 입력
# input("안내_문구")
number = input("숫자를 입력하세요: ")
print(number)
# input은 문자열 취급을 함으로 숫자가 아닌 문자열 타입이라는 것을 주의.
print("type(number) : ", type(number))

# 입력 값을 숫자로 대입.
# int() 함수 : 문자열이나 실수를 정수로 변환하는 파이썬 내장 함수
age = input("나이를 입력하세요: ")
age = int(age)
print("age + 1 : ", age + 1)

# float() 함수 : 문자열이나 정수를 실수로 변환하는 파이썬 내장 함수
height = input("키를 입력하세요(cm): ")
height = float(height)
# ⭐ 왜 ??? 이렇게 나오지..???
# 키를 입력하세요(cm): 161.2
# height :  1.611999999999999
print("height : ", height / 100)

# input과 int(또는 float)를 한 줄에 작성 가능
age = int(input("나이를 입력하세요: "))
print("type(age) : ", type(age))

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")  # 1번
print("life"+"is"+"too short")  # 2번

# 문자열 띄어쓰기는 쉼표로 한다
print("life", "is", "too short")

# sep 매개변수로 구분자 설정하기
# 출력할 값들 사이의 구분자를 지정 가능.
print("2025", "08", "17", sep="-")
print("점프", "투", "파이썬", sep=" TO ")

# 한 줄에 결괏값 출력하기
# 한 줄에 결괏값을 이어서 출력하려면 end 매개변수를 사용해 끝 문자를 지정 필요.
for i in range(10):
    print(i, end=' ')

# calculator.py
print("=== 간단한 계산기 ===")

# 사용자로부터 두 숫자 입력받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 계산 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")
