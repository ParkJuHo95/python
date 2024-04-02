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
        print("생성자")
        
    def named(self,name):   #첫번째 인자부분에 self를 넣은것은 문법적인 부분
        self.name = name
    
    def __str__(self):      #toString 역할
        return "[Animal][name]:"+self.name
    
    def __del__(self):      #자바에서는 가비지컬렉션이 있어 알아서 메모리 관리를 해주지만 다른 언어들은 없기 때문에 소멸자를 만들어서 메모리 관리를 해줘야 함
        print("소멸자")
        

class Human(Animal):
    def __init__(self):
        super().__init__()  #컴파일 하는 과정이 없어서 super를 자동적으로 넣어주지 않음 따라서 수퍼를 직접 적어줘야 전역변수까지 상속을 받음
        self.asset = 0
        # self.name = "";
        
    def goldspoon(self):
        self.asset = 10000000000
        
    def __del__(self):
        print("소멸자")
        
if __name__ == '__main__':      #메인으로 실행해줘야 나중에 이 클래스를 import하여 쓸때 main에서 실행한것이 다시 실행되지 않는다 main에서 실행하지 않고 그냥 실행하면 import해서 실행할때 실행했던것이  다시 실행됨
    
    hum = Human()
    print("name :", hum.name)
    print("asset :", hum.asset)
    hum.named("개똥이")
    hum.goldspoon()
    print("name :" , hum.name)    
    print("asset :", hum.asset)
    
    
        
    
    
    
    