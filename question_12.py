# my_module 폴더에 my_module.py 파일을 만들어 아래의 함수를 정의하고, 이를 import하여 사용하시오.
# def my_calculator(a, operator, b):
#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a - b
#     elif operator == "*":
#         return a * b
#     else:
#         return "잘못된 연산자입니다."

# 주의 ) 이 파일의 코드를 수정하지 마세요.

from my_module.my_calculator import my_calculator

def question12():
    print("7 + 5", my_calculator(7, "+", 5))
    print("7 - 5", my_calculator(7, "-", 5))
    print("7 * 5", my_calculator(7, "*", 5))

question12()