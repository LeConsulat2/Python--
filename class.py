class University:
    def __init__(self, ability, character, years_of_service):
        self.ability = ability
        self.character = character
        self.Service_Years = years_of_service

    def sleep(self):
        print("zzzzzz......")

class Tenured_직원(University):
    def __init__(self, ability, character):
        super().__init__(ability, character, 25)
        
    def when_asked(self):
        print("Seriously, one more request to me, I am out of here")

    def when_approached(self):
        print(f"Dont forward emails to me, you know I can get it done quick as I am {self.ability}") 
        self.when_asked()        
           
class Newbie_직원(University):

    def __init__(self, ability, character):
        super().__init__(ability, character, 1)

    def when_asked(self):
        print("Anytime, please")

    def when_approached(self):
        print(f"My name is 사라 and yes I will work overtime, as I am {self.ability}") 
        self.when_asked()    

벤 = Tenured_직원("개고수", "이성적")
사라 = Newbie_직원("개씹초보", "감성적")


사라.when_approached()
벤.when_approached()
벤.sleep()

print(사라.ability, 사라.character, 사라.Service_Years)
print(벤.ability, 벤.character, 벤.Service_Years)

#space-------------------------------------------

class AUT_직원:

    def __init__(self, level, character, age):
        self.level = level
        self.age = age
        self.type = character

    def __str__(self):
        return f"AUT_직원 named {self.level}, type: {self.type}"
# def __str__(self): 는 console에 나오게 할려고 User가 보이진않음. 여기 밑에 value 넣으셈

리즈 = AUT_직원("", "", 52)
세실리아 = AUT_직원("", "", 50)

print(리즈.level, 리즈.type, 리즈.age)
