# 3차원 좌표의 위치를 가지는 3차원 위치 클래스를 완성하고,
# 3차원 좌표의 덧셈과 뺄셈을 구현하세요.
# 또한 두 개의 3차원 좌표의 사이의 거리를 구하는 기능도 구현하세요.
# 3차원 좌표의 위치는 x, y, z 값을 가지며, 거리는 두 점 사이의 거리를 의미합니다.
# 두 점 사이의 거리는 다음과 같이 구할 수 있습니다.
# 두 점 사이의 거리 = 루트((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
# 그리고 다음 코드를 실행했을 때 다음과 같이 출력되도록 클래스를 완성하세요.
# point1 = Point3D(1, 2, 3)
# point2 = Point3D(4, 5, 6)

# print(point1 + point2)
# print(point1 - point2)

# 출력 예시
# (5, 7, 9)
# (-3, -3, -3)
# 5.196152422706632

# 주의) todo 주석이 있는 부분만 작성하세요

import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def inverse(self):
        return Point3D(-self.x, -self.y, -self.z)
    
    def __add__(self, other):
        if isinstance(other, Point3D):
            pass # todo : 코드를 작성하여 두 Point3D 객체의 덧셈을 구현하세요.
        raise Exception("Point3D 객체가 아닙니다.")
    
    def __sub__(self, other):
        # todo: 빼는 연산자를 구현하세요.
        pass
    
    def distance(self, other):
        if isinstance(other, Point3D):
            pass # todo : 코드를 작성하여 두 Point3D 객체 사이의 거리를 구하세요.
        raise Exception("Point3D 객체가 아닙니다.")


def question_8():
    point1 = Point3D(1, 2, 3)
    point2 = Point3D(4, 5, 6)

    print(point1 + point2)
    print(point1 - point2)

    print(point1.distance(point2))

question_8()