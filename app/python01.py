## hello.py
print("=" * 25 + " 시작 " + "=" * 25)
print("Hello VS Code !!")

## python 
print("=" * 25 + " 정수, 실수, 8진수, 16진수 " + "=" * 25)
a = 123
print("정수형: " + str(a))
a = -123
print("정수형: " + str(a))

## 실수형
a = 1.2
print("실수형: " + str(a))
a = 4.24E10
print("실수형: " + str(a))
a = 4.24e-10
print("실수형(4.24e-10): " + str(a))

## 8진수(octal) 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)로 시작
a = 0o177
print("8진수(0o177): " + str(a))

## 16진수(hexadecimal) 0x로 시작
a = 0x8ff
b = 0xABC
print("16진수(0x8ff): " + str(a))
print("16진수(0xABC): " + str(b))

## 사칙 연산
print("=" * 25 + " 사칙 연산 " + "=" * 25)
a = 3
b = 4
print("사칙 연산(a = 3, b = 4)")
print("사칙 연산(+): " + str(a + b))
print("사칙 연산(-): " + str(a - b))
print("사칙 연산(*): " + str(a * b))
print("사칙 연산(/): " + str(a / b))
print("사칙 연산(%): " + str(a % b))
print("사칙 연산(**): " + str(a ** b))
print("사칙 연산(//): " + str(a // b))

# 문자열 자료형
print("=" * 25 + " 문자열 자료형 " + "=" * 25)
food = "Python's favorite food is perl"
print("문자열 자료형 : " + food)
food = 'Python\'s favorite food is perl'
print("문자열 자료형 : " + food)
say = '"Python is very easy." he says.'
print("문자열 자료형 : " + say)
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(say)
print(food)
multiline = "Life is too short\nYou need python"
print("역슬래시 n : " + multiline)
multiline='''
Life is too short
You need python
'''
print("작은 따옴표 3개 : " + multiline)
multiline="""
Life is too short
You need python
"""
print("큰 따옴표 3개 : " + multiline)
print()
head = "Python"
tail = " is fun!"
print(head + tail)

print("-" * 10 + " 문자열 슬라이싱 " + "-" * 10)
a = "Life is too short"
print("len(a): " + str(len(a)))

a = "Life is too short, You need Python"
print("a[3]: " + str(a[3]))
print("a[0:4]: " + str(a[0:4]))
print("a[-1]: " + str(a[-1]))

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print("b: " + b)
print("a[19:]: " + a[19:])
print("a[:17]: " + a[:17])

print("-" * 10 + " 문자열 슬라이싱 " + "-" * 10)
a = "20230331Rainy"
year = a[:4]
date = a[:8]
weather = a[8:]
print("date: " + date)
print("weather: " + weather)

print("-" * 10 + " 문자열 포매팅 " + "-" * 10)
print("숫자 바로 대입 : " + "I eat %d apples." % 3)
print("문자열 바로 대입 : " + "I eat %s apples." % "five")
number = 3
fruit = "apple"
print("문자열 바로 대입 : " + "I eat %d apples." % number)
number = 10
day = "three"
print("문자열 바로 대입 : " + "I ate %d apples. so I was sick for %s days." % (number, day))

## 문자열 포맷 코드 
# %o : 8진수
# %x : 16진수
# %g : 값에 따라 %f 또는 %e 중 하나를 자동으로 선택
# %p : 포인터 값
# %n : 버퍼에 저장된 문자 수
# %% : % 문자 자체
"%10s" % "hi"
print("\"%10s\" % \"hi\" : " + "%10s" % "hi")
"%-10sjane." % 'hi'
print("\"%-10sjane.\" % 'hi' : " + "%-10sjane." % 'hi')

"%0.4f" % 3.42134234
print("\"%0.4f\" % 3.42134234 : " + "%0.4f" % 3.42134234)

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number = 3
print("I eat {0} apples".format(number))
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

print("-" * 10 + " 정렬 " + "-" * 10)
print("왼쪽 정렬 : {0:<10}".format("hi"))
print("오른쪽 정렬 : {0:>10}".format("hi"))
print("가운데 정렬 : {0:^10}".format("hi"))
print("공백 채우기 : {0:=^10}".format("hi"))
print("공백 채우기 : {0:!<10}".format("hi"))
print("공백 채우기 : {0:05d}".format(5))
print("공백 채우기 : {0:05d}".format(-5))
print("공백 채우기 : {0:05d}".format(10))
print("공백 채우기 : {0:05d}".format(100))
print("공백 채우기 : {0:05d}".format(1000))

y = 3.42134234
print("-" * 10 + " 소수점 표현 " + "-" * 10)
print("\"{0:0.4f}\".format(y) : " + "{0:0.4f}".format(y))

print("-" * 10 + " { 또는 } 문자 표현 " + "-" * 10)
print("{{ and }}".format())

print("-" * 10 + " f 문자열 포매팅 " + "-" * 10)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age + 1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print("-" * 10 + " 문자열 관련 함수 " + "-" * 10)
a = "hobby"
print("a.count('b') : " + str(a.count('b')))

a = "Python is the best choice"
print("a.find('b'): " + str(a.find('b')));
print("a.find('k'): " + str(a.find('k')));

print("\",\".join('abcd')" + ",".join('abcd'))

a = "hi"
print("a: "+ a)
print("a.upper(): " + a.upper())
a = "HI"
print("a: "+ a)
print("a.lower(): " + a.lower())

a = " hi "
print("a: "+ a)
print("a.lstrip(): " + a.lstrip())
print("a.rstrip(): " + a.rstrip())

a = "Life is too short"
print("a: "+ a)
print("a.replace(\"Life\", \"Your leg\"): " + a.replace("Life", "Your leg"))
a.split()
print("a.split(): "+ str(a.split()))
b = "a:b:c:d"
b.split(':')
print("b: "+ b)
print("b.split(':'): "+ str(b.split(':')))

# isalpha : 
# 문자열이 알파벳으로만 구성되어 있는지 확인 
# 공백이나 숫자, 특수 문자가 포함되어 있으면 False
s = "Python"
print(s + ": " + str(s.isalpha()))
s = "Python3"
print(s + ": " + str(s.isalpha()))
s = "Hello World"
print(s + ": " + str(s.isalpha()))

# isdigit : 
# 문자열이 숫자(0~9)로만 이루어져 있는지를 검사
# 하나라도 숫자가 아닌 문자가 포함되어 있으면 False를 반환
s = "12345"
print("s:" + s)
print("s.isdigit(): " + str(s.isdigit()))
s = "1234a"
print("s:" + s)
print("s.isdigit(): " + str(s.isdigit()))
s = "12 34"
print("s:" + s)
print("s.isdigit(): " + str(s.isdigit()))

s = "Life is too short"
print("s:" + s)
print("s.startswith(\"Life\"): " + str(s.startswith("Life")))
print("s.startswith(\"short\"): " + str(s.startswith("short")))
print("s.endswith(\"short\"): " + str(s.endswith("short")))
print("s.endswith(\"too\"): " + str(s.endswith("too")))