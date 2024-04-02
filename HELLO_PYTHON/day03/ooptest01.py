# class Animal:
#     name = "";
    # def named(name1):  # @NoSelf
#         return name1;
# name = Animal.name
# print("name : ",name)
#
# name = Animal.named("가나")
# print("name : ",name)

class Animal:
    def __init__(self):     #파이썬에서 생성자
        self.name = ""
        
    def named(self,name):   #첫번째 인자부분에 self를 넣은것은 문법적인 부분
        self.name = name
        
        
if __name__ == '__main__':      #메인으로 실행해줘야 나중에 이 클래스를 import하여 쓸때 main에서 실행한것이 다시 실행되지 않는다 main에서 실행하지 않고 그냥 실행하면 import해서 실행할때 실행했던것이  다시 실행됨
    ani = Animal()
    print("ani.name :", ani.name)
    ani.named("멍멍이")
    print("ani.name :", ani.name)