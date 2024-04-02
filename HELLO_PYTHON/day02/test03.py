# 출력할 단수를 입력하세요
# 2*1=2
# .
# .
# .
# 2*9=18

# a = int(input("출력할 단수를 입력하세요"))
#
# for i in range(1,9+1) :
#     print("{}*{}={}".format(a,i,i*a))

##########################################
a = input("출력할 단수를 입력하세요")

aa = int(a)

for i in range(1,9+1) :
    # print(a+"*"+str(i)+"="+str(aa*i))
    print("{}*{}={}".format(a,i,aa*i))
    