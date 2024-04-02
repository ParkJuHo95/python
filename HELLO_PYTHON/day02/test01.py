# 1에서 10까지의 합을 구하시오

arr = range(1, 10 + 1)

sum = 0;

for i in arr:
    sum += i

print(sum)

sum1 = 0;

arr1 = list(arr)
for i in arr1:
    sum1 += arr1[i - 1]
    
print(sum1)

##############################################################
# 선생님 풀이

sum2 = 0
for i in range(1, 10 + 1):
    sum2 += i
    
print("sum", sum2)
