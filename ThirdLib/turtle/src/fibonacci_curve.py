"""
Name : fibonacci_curve.py
Author : Barbara
Time : 2022/12/6 下午4:45
Desc :
"""
import turtle

if __name__ == "__main__":
    # a, b = 0, 0.1
    a, b = 0, 1
    while a < 1000:
        turtle.circle(a, 90)
        a, b = b, a + b