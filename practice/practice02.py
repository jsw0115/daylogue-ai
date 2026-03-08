# 연습문제 02

# 01. 
print()
print("====================================================================================")
print()
print("01. 다음 코드의 결과 값")
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a : print("need")
else: print("none")
print("답 : shirt"); 
print()

# 02. 
print()
print("====================================================================================")
print()
print("02. while 문을 사용해 1 ~ 1000 자연수 중 3의 배수의 합")
result = 0
i = 1
while i <= 1000: 
    if i%3 == 0:
        result += i
    i += 1
print("result ? ", result); 
print()

# 03. 
print()
print("====================================================================================")
print()
print("03. while 문 사용해 *을 표시하는 프로그램")
i = 0
while True:
    i += 1
    if i > 5 : break
    print("*" * i)
print()

# ⭐ 04. 
print()
print("====================================================================================")
print()
print("⭐ 04. for 문을 사용해 1 ~ 100 숫자 출력")
for i in range(1, 101):
    print(i)
# print("result ? ", result); 
print()

# ⭐ 05. 
print()
print("====================================================================================")
print()
print("⭐ 05. for문을 사용해 A 학급의 평균 점수 구하기")
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
# average = total / A.count (오답!)
average = total / len(A)
# A 의 길이 : 
average = total
print("average : ", average)
print()

# ⭐ 06. 
print()
print("====================================================================================")
print()
print("⭐ 06. 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드. 리스트 내포를 사용하여 표현.")
numbers = [1,2,3,4,5]
result = []
for n in numbers : 
    if n%2 == 1:
        result.append(n*2)
print("result ? ", str(result)); 

numbers = [1,2,3,4,5]
result = [num * 2 for num in numbers if num % 2 == 1]
print("result ? ", str(result)); 

print()