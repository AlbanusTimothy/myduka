# 2.Create a Schoo system program using Python classes to demnstraate inheritance
# -Create a parent class called Person with:
#     attributes - name , age 
#     method : displaay_info()

# -> Create child classes that inherit the parent class:
#        a)Student with:
#              -additional attributes - student_id, course
#              -override display_info() to include student_id and course
#        b)Teacher with:
#               -additional attributes - subject, salary
#               -override display_info() to include subject and salary
# -----------------school programme---------------------------


# parent class-person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# child class-student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}, Course: {self.course}"
        )

# child class-teacher
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Subject: {self.subject}, Salary: {self.salary}"
        )
# runnnnn it
student1 = Student("Alba", 20, "S123", "Computer Science")
teacher1 = Teacher("Mr. Kamau", 40, "Mathematics", 85000)

print(student1)   
print(teacher1)   
