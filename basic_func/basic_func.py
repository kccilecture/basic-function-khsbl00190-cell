import math

def add(a, b):
    return (a+b)


def sub(a, b):
    return (a-b)


def mul(a, b):
    return (a*b)


def div(a, b):
    return(a/b)


def power(base, pow):
    return base ** pow


def square(base):
    return base ** 2

result = square(100)
print(result)  # 결과: [10.0, -10.0]


def greet(이름="낯선자", 나이=20):
    if 나이 < 5:
        return f"안녕 {이름}!"
    
    elif 나이 >= 50:
        return f"안녕하십니까 {이름}!"
    
    else:
        return f"안녕하신가 {이름}!"
