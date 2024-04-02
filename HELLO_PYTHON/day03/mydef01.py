#자바에서는 class 파일을 만들어서 읽기 때문에 다 읽은 상태로 불러오는 것이라 메소드가 밑에 정의 되어있어도 상관이 없지만
#파이썬에서는 인터프리터방식(위에서 아래 순)으로 실행하기 때문에 정의가 미리 되어있지 않으면 실행오류가 난다

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def remain(a,b):
    return a%b

sum = add(4,2)
min = minus(4,2)
mul = multiply(4,2)
div = divide(4,2)
remain = remain(4,2)

print("sum :",sum)
print("min :",min)
print("mul :",mul)
print("div :",div)
print("remain :",remain)

