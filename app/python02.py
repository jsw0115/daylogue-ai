# 리스트 자료형
# 리스트명 = [요소1, 요소2, 요소3, 요소4]
print("=" * 25 + " 리스트 자료형 " + "=" * 25)
odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 비어 있는 리스트 생성 방법 
# → a = list()

# 리스트의 인덱싱과 슬라이싱 
# a[0] : a 리스트의 첫 번쨰 요소.
# a[-1] : a 리스트의 마지막 요소. 
print("")
print("=" * 25 + " 리스트의 인덱싱과 슬라이싱 " + "=" * 25)
a = [1, 2, 3, ['a', 'b', 'c']]
print("a : " + str(a))
# a[-1]
print("a[-1] : " + str(a[-1]))
# a[3]
print("a[3] : " + str(a[3]))
# a[-1][0]
print("a[-1][0] : " + str(a[-1][0]))

# 삼중 리스트에서 인덱싱.
print("") 
print("=" * 25 + " 삼중 리스트에서 인덱싱 " + "=" * 25)
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print("a : " + str(a))
# a 안에 리스트 하나 (['a', 'b', ['Life', 'is']]) 가 포함되어 있음.
# 그 리스트 안에 또 다른 리스트(['Life', 'is'])가 포함되어 있음. 
# 즉, 삼중 리스트 형태. 
a[2][2][0]
print("a[2][2][0] : " + str(a[2][2][0]))

# 리스트의 슬라이싱. 
print("")
print("=" * 25 + " 리스트의 슬라이싱 " + "=" * 25)
a = [1, 2, 3, 4, 5]
print("a : " + str(a))
a[0:2]
print("a[0:2] : " + str(a[0:2]))

a = "12345"
print("a : " + str(a))
a[0:2]
print("a[0:2] : " + str(a[0:2]))

a = [1, 2, 3, 4, 5]
print("a : " + str(a))
b = a[:2]
print("b : " + str(b))
c = a[2:]
print("c : " + str(c))

# 중첩된 리스트에서 슬라이싱. 
print("")
print("=" * 25 + " 중첩된 리스트에서 슬라이싱 " + "=" * 25)
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print("a : " + str(a))
a[2:5]
print("a[2:5] : " + str(a[2:5]))
a[3][:2]
print("a[3][:2] : " + str(a[3][:2]))

# 리스트 연산. 
print("")
print("=" * 25 + " 리스트 연산 " + "=" * 25)
a = [1, 2, 3]
print("a : " + str(a))
b = [4, 5, 6]
print("b : " + str(b))
a + b
print("a + b : " + str(a + b))

# 리스트 반복.
print("")
print("=" * 25 + " 리스트 반복 " + "=" * 25)
a = [1, 2, 3]
a * 3
print("a : " + str(a))
print("a * 3 : " + str(a * 3))

# 리스트 길이 구하기.
print("")
print("=" * 25 + " 리스트 길이 " + "=" * 25)
a = [1, 2, 3]
print("a : " + str(a))
len(a)
print("len(a) : " + str(len(a)))

# ☆ 리스트 연산 오류. 
print("")
print("=" * 25 + " 리스트 연산 " + "=" * 25)
# 정수에 더하기 문자열을 하는 순간. 서로 더할 수 없어 오류 발생. 
# → 숫자 3을 문자 '3'으로 변경 필요. 
a = [1, 2, 3]
print("a : " + str(a))
# a[2] + "hi"
# 오류 발생 ! 
str(a[2]) + "hi"
print("str(a[2]) + \"hi\" : " + str(str(a[2]) + "hi"))

# 리스트 값 수정.
print("")
print("=" * 25 + " 리스트 값 수정정 " + "=" * 25)
a = [1, 2, 3]
print("a : " + str(a))
a[2] = 4
print("AFTER a[2] = 4 → " + str(a))
a

# 리스트 요소 삭제.
print("")
print("=" * 25 + " 리스트 요소 삭제 " + "=" * 25)
# del a[x] : x 번째 요솟값 삭제. 
# del 은 파이썬이 기본 제공하는 명령어. 객체 삭제 시, 사용. 
# del 객체. 
a = [1, 2, 3]
print("a : " + str(a))
del a[1]
print("del a[1] : " + str(a))
# del 리스트 요소 삭제 
# 두번쨰 요솟값에서 마지막 요소까지 삭제. 
print("")
a = [1, 2, 3, 4, 5]
print("a : " + str(a))
del a[2:]   
print("del a[2:] : " + str(a))
a

# 리스트 관련 함수. 
print("=" * 25 + " 리스트 관련 함수 " + "=" * 25)
print("")
print("** append **")
# 리스트 요소 추가 : append 
# 마지막에 요소 추가. 
a = [1, 2, 3]
print("a : " + str(a))
a.append(4)
print("a.append(4) : " + str(a))

# 리스트 정렬 : sort
print("")
print("** sort **")
# 리스트 숫자 혹은 문자 순서대로 정렬.
a = [1, 4, 3, 2]
print("a : " + str(a))
a.sort()
print("a.sort() : " + str(a))
print("")
a = ['a', 'c', 'b']
print("a : " + str(a))
a.sort()
print("a.sort() : " + str(a))
a

# 리스트 뒤집기 : reverse
print("")
print("** reverse **")
# 리스트 요소를 순서대로 정렬 후, 역순으로 정렬하는 것이 아닌, 
# "현재의 리스트"를 "그대로" 거꾸로 뒤집음. 
a = ['a', 'c', 'b']
print("a : " + str(a))
a.reverse()
print("a.reverse() : " + str(a))
a

# 인덱스 반환 : index
print("")
print("** index **")
a = [1, 2, 3]
print("a : " + str(a))
a.index(3)
print("a.index(3) : " + str(a.index(3)))
a.index(1)
print("a.index(1) : " + str(a.index(1)))
#  리스트에 존재하지 않으면 오류가 발생
# a.index(0)

# 리스트 삽입 : insert
print("")
print("** insert **")
a = [1, 2, 3]
print("a : " + str(a))
a.insert(0, 4)  # a[0] 자리에 4 삽입.
print("a.insert(0, 4) : " + str(a))
# a
a.insert(3, 5)  # a[3] 자리에 5 삽입.
print("a.insert(3, 5) : " + str(a))
# a

# 리스트 요소 제거 : remove
# remove(x) 는 리스트에서 첫 번째로 나오는 x를 삭제. 
print("")
print("** remove **")
a = [1, 2, 3, 1, 2, 3]
print("a : " + str(a))
a.remove(3)
print("a.remove(3) : " + str(a))

# 리스트 요소 꺼내기 : pop
# 리스트의 맨 마지막 요소를 반환하고 해당 요소는 삭제. 
# pop(x) 는 리스트 x 번째 요소를 반환 후, 해당 요소는 삭제. 
print("")
print("** pop **")
a = [1, 2, 3]
print("a : " + str(a))
a.pop()
print("a.pop() : " + str(a.pop()))
print("a : " + str(a))
a = [1, 2, 3]
print("AFTER a : " + str(a))
print("")
a.pop(1)
print("a.pop(1) : " + str(a.pop(1)))
a

# 리스트 포함된 요소 x의 개수 세기 : count 
print("")
print("** count **")
a = [1, 2, 3, 1]
print("a : " + str(a))
a.count(1)
print("a.count(1) : " + str(a.count(1)))

# 리스트 확장 : extend 
print("")
print("** extend **")
# extend(x)에서 x에는 리스트만 가능. 
a = [1, 2, 3]
print("a : " + str(a))
a.extend([4, 5])
print("a.extend([4, 5]) : " + str(a))
# a
b = [6, 7]
print("b : " + str(b))
a.extend(b)
print("a.extend(b) : " + str(a))
a
# a.extend([4,5]) 는 a += [4,5] 와 동일.

# 딕셔너리.
print("")
print("")
print("=" * 25 + " 딕셔너리 " + "=" * 25)
# 사전이라는 뜻. 
# Key 와 Value 한 쌍으로 가지는 자료형. 
# 리스트나 튜플처럼 순차적으로 요솟값을 구하는 것이 아닌, Key를 통해 Value를 얻음. 
# 파이썬 3.7 이잔, 딕셔너리에 데이터를 저장할 때, 입력한 순서가 보장되지 않음.
# 파이썬 3.7 부터, 아이템을 삽입한 순서가 유지.
# 즉, 딕셔너리를 순회 시, 아이템이 추가된 순서대로 나옴. 
# 딕셔너리 기본 구조 ex. {Key1: Value1, Key2: Value2, Key3: Value3, ...}
a = {1: 'hi'}
print("a : " + str(a))
a = {'a': [1, 2, 3]}
print("a : " + str(a))

# 딕셔너리 쌍 추가 및 삭제. 
print("")
print("=" * 25 + " 딕셔너리 쌍 추가 및 삭제 " + "=" * 25)
a = {1: 'a'}
print("a : " + str(a))
a[2] = 'b'
print("AFTER a[2] = 'b' : " + str(a))
a['name'] = 'pey'
print("AFTER a['name'] = 'pey' : " + str(a))
a[3] = [1, 2, 3]
print("AFTER a[3] = [1, 2, 3] : " + str(a))
del a[1]
print("AFTER del a[1] : " + str(a))

# 어떤 Key의 Value를 얻으려면 '딕셔너리_변수_이름[Key]'를 사용
grade = {'pey': 10, 'julliet': 99}
grade['pey']
print("grade['pey'] : " + str(grade['pey']))

# 주의 사항. 
# 딕셔너리에서 Key는 고유의 값으로, 중복되는 Key 값을 설정하면 하나를 제외한 나머지 것들이 무시된다. 
a = {1:'a', 1:'b'}
print("a : " + str(a))
# Key에 리스트는 사용할 수 없다. 튜플은 사용 가능하다. 
# Key는 변하는 값이라면 Key 로 사용이 불가하고, 불변의 값이라면 사용이 가능하다. 
# 오류 발생 !! 
# a = {[1,2] : 'hi'}

# 딕셔너리 관련 함수. 
print("=" * 25 + " 딕셔너리 관련 함수 " + "=" * 25)

# Key 리스트 만들기 : keys 
print("")
print("** keys **")
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print("a : " + str(a))
a.keys()
print("a.keys() : " + str(a.keys()))
# 딕셔너리 a의 Key 만을 모아 dict_keys 객체를 반환. 
# 2.7 버전까지는 리스트를 반환했다. 
# 리스트를 반환하면 메모리 낭비가 발생.
# 해당 메모리 낭비를 줄이기 위해 dict_keys 객체를 반환하도록 변경.
# 3.0 이후 버전에서는 dict_values, dict_items 들이 추가. 
# 반환값으로 리스트가 필요한 경우 : list(a.keys()) 사용
# dict_keys, dict_values, dict_items는 기본적인 반복구문에 사용 가능. 
# 리스트 고유 함수는 수행 불가 : append, insert, pop, remove, sort
for k in a.keys():
    print(k)    # 들여쓰기를 하지 않으면 오류 발생 !!! 

# dict_keys 객체를 리스트로 변환하는 방법 
list(a.keys())
print("list(a.keys()) : " + str(list(a.keys())))

# Value  리스트 만들기 : values 
print("")
print("** values **")
a.values()
print("a.values() : " + str(a.values()))

# Key, Value 쌍 얻기 : items
# Key와 Value 쌍을 튜플로 묶은 값을 dict_items 객체로 반환. 
print("")
print("** items **")
a.items()
print("a.items() : " + str(a.items()))

# Key, Value 쌍 모두 지우기 : clear 
# 딕셔너리 안 모든 요소 삭제. 
# 빈 딕셔너리 : {} 
print("")
print("** clear **")
a.clear()
print("AFTER a.clear() : " + str(a))

# Key로 Value 얻기 - get 
print("")
print("** get **")
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print("a : " + str(a))
a.get('name')
print("a.get('name') : " + str(a.get('name')))
# 딕셔너리에 존재하지 않은 키로 값을 가져올 경우, None을 반환. 
a.get('nokey')
# 아래 오류 발생. 
# a['nokey']
print("a.get('nokey') : " + str(a.get('nokey')))
# 딕셔너리 안에 Key가 없을 경우, 디폴트 값을 대신 가져오고 싶을 경우, 
a.get('nokey', '정보 없음')
print("a.get('nokey', '정보 없음') : " + str(a.get('nokey', '정보 없음')))

# Key가 딕셔너리 안에 있는지 조사 : in
print("")
print("** in **")
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print("a : " + str(a))
'name' in a
print("'name' in a : " + str('name' in a))
'email' in a
print("'email' in a : " + str('email' in a))

# Key로 Value 얻기 : pop
# Key가 x인 항목을 삭제한 후 그 Value 반환
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
print("phone : " + str(phone))
print("a : " + str(a))