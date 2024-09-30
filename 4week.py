#퀴즈 1번
user_input = input("입력하세요")
if user_input == "안녕하세요" :
    print("반갑습니다.")
else:
    print("인사를 먼저하세요.")


#퀴즈 2번
number = input("숫자를 입력하세요")
a = int(number) + 100

if a >= 150 :
    print(a)
else:
    print("값이 부족합니다.")


#퀴즈 3번
numbers = [100,200,300]
result = []

for i in numbers :
    price = i * 1.1
    result.append(price)

print(result)


#퀴즈 4번
numberss = [3,100,23,33,72,94]
final = []

for e in numberss :
    if e % 3 == 0 :
        final.append(e)

print(final)

#퀴즈 5번
b = 0

while b <= 999 :
    b = b + 1
    print(f"대기번호 : {b} ")

#퀴즈 6번
c = 0
d = 0
while c <= 100 :
    if c % 2 != 0 :
        d += c
    c = c + 1

print(f"1~100 중 홀수의 합 : {d}")
