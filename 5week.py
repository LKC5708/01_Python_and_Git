#퀴즈 1번
from sys import setswitchinterval


def add(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

add_d = add(1,2,3,4)
print(add_d)

def multiply(a, b, c, d):
    result = a * b * c * d
    return result

multiply_d = multiply(1,2,3,4)
print(multiply_d)

#퀴즈 2번
def hol(num):
    if num % 2 == 0 :
        return "짝수"
    else:
        return "홀수"
hol_d = hol(4)
print(hol_d)

#퀴즈 3번
def average(num):
    length = len(num)
    total = 0
    for i in num:
        total += i
    return total/len(num)
average_d = average([1,2,3,4,5,6])
print(average_d)

#퀴즈 4번
class GameCharacter:
    def __init__(self,id,gender,job):
       self.id = id
       self.gender = gender
       self.job = job

    def attack(self):
        print("공격!")

character = GameCharacter("LKC","남성","전사")
character.attack()

#뮈즈 5번
class RealEstate:
    def __init__(self,location,size,type,price,year):
        self.location = location
        self.size = size
        self.type = type
        self.price = price
        self.year = year

    def show(self):
        print(f"위치 : {self.location}")
        print(f"평수 : {self.size}")
        print(f"건물 종류 : {self.type}")
        print(f"가격 : {self.price}만원")
        print(f"건축연도 : {self.year}")

gest = RealEstate("인천 중구",30,"아파트",50,2009)
gest.show()

