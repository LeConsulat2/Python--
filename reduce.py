class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [student("JP", 60), student("Sophie", 98), student("Jack", 45) ] 

score_total = 0
for student in students:
    score_total +=  student.score
#You could also do score_total = sum(student.score for student in students)

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total, students, 0)

print(round(reduce_total / len(students)), )   