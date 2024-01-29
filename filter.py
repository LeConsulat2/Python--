class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"   
    
students = [student("JP", 0.50), student("Amy", 0.69), student("Mark", 0.90)]


failing_students = []
for student in students:
    if student.score < 0.70:
        failing_students.append(student)

filter_list = list(filter(lambda student: student.score < 0.70, students))

print(filter_list)

#filter even numbers

numbers = [1,2,3,4,5]

print(list(filter(lambda number: number % 2 == 0, numbers)))


   