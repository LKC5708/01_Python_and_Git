# 퀴즈 1번
import random

def random_lotto():
    result = []
    while len(result) < 6:
            num = random.randint(1,45)
            if num not in result:
                result.append(num)
    return result
print(random_lotto())

#퀴즈 2번
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1,10):
            print(f"{self.num} X {i} = {self.num * i}")

two_dan = Gugudan(2)
two_dan.output()

#퀴즈 3번
# 저는 평소 자동차를 좋아히기에 스마트크루즈 컨트롤 시스템 중 앞차량과 거리가 가까워지면 브레이크를 작동시키는 코드를 생각해 봤습니다.
class Vehicle:
    def __init__(self, name, speed=0):
        self.name = name  # 차량 이름
        self.speed = speed  # 차량 속도
        self.distance_to_front_vehicle = float('inf')  # 앞차와의 거리

# 차량 속도를 설정하는 함수
    def set_speed(self, speed):
        self.speed = speed
        print(f"차량 속도가 {self.speed} km/h로 설정되었습니다.")

# 앞 차와의 거리를 설정하는 함수
    def set_distance(self, distance):
        self.distance_to_front_vehicle = distance
        print(f"앞 차와의 거리를 {self.distance_to_front_vehicle} 미터로 설정했습니다.")

#충돌 위험 함수
    def check_risk(self):
        if self.distance_to_front_vehicle < 5:  # 5미터 미만일 경우 충돌 위험
            print("경고: 충돌위험 감지 브레이크 작동 요망")
            self.activate_brake()

#브레이크 작동 함수
    def activate_brake(self):
        print("자동 브레이크 작동")


vehicle1 = Vehicle("로체 이노베이션")
vehicle1.set_speed(80)

# 앞차와의 거리 설정 및 충돌 위험 체크
vehicle1.set_distance(3)  # 앞차와의 거리를 3미터로 설정
vehicle1.check_risk()  # 충돌 위험 체크
