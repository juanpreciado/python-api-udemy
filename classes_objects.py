class LotteryPlater:
    def __init__(self, name):
        self.name = name
        self.numbers = (8,10,12,1,21) 
    
    def total(self):
        return sum(self.numbers)

player = LotteryPlater('Juanillo')
print(player.name)
print(player.numbers)
print(player.total())

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len (self.marks)    

anna = Student('Anna', 'MIT')
anna.marks.append(50)
anna.marks.append(60)
print(anna.average())