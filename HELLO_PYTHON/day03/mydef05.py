#자바에서 메서드는 return값이 없거나 하나밖에 되지 않지만 파이선은 여러개의 값을 리턴 가능

def add_min_mul_div(a,b):
    return a+b,a-b,a*b,a/b


sum,min,mul,div = add_min_mul_div(4,2)

print("sum :",sum)
print("min :",min)
print("mul :",mul)
print("div :",div)

sum1 = add_min_mul_div(4,2)
print(sum1)     #튜플(배열과 비슷하지만 더 작은 범위라고 생각하면 됨) 사용법은 배열과 같음
print(sum1[2])
