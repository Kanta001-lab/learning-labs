class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.courses = []

class Course:
    def __init__(self, title, credits):
        self.title = title
        self.credits = credits
        self.grades = {}

class Department:
    def __init__(self, name):
        self.name = name
        self.course = []

class School:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []


# BUILDING THE DATA (OBJECT GRAPH)

# Create addresses
addr1 = Address("Lagos", "Allen Avenue")
addr2 = Address("Abuja", "Ahmadu Bello Way")
addr3 = Address("Ibadan", "Ring road")


# Create students
esther = Student("Esther", 20, addr1)
hassan = Student("Hassan", 22, addr2)
ali = Student("Ali", 21, addr3)


# Create courses
math = Course("Calculus", 3)
physics = Course("Physics", 4)
history = Course("History", 3)


# Enroll students in course
esther.courses = [math, physics]
hassan.courses = [math, history]
ali.courses = [physics, history]


# Add grades
math.grades = {"Esther": 95, "Hassan": 82}
physics.grades = {"Esther": 88, "Ali": 91}
history.grades = {"Hassan": 78, "Ali": 85}


# Create department
science_dept = Department("Science")
science_dept.course = [math, physics]

humanities_dept = Department("Humanities")
humanities_dept.course = [history]


# Create school
school = School("Python High")
school.departments = [science_dept, humanities_dept]
school.students = [esther, hassan, ali]


# 1. Get the city of the first student
print(school.students[0].address.city)  # "Lagos"
# Steps: school -> student list -> first student -> address -> city

# 2. Get the title of the second course of the second student
print(school.students[1].courses[1].title)  # "History"
# Steps: school -> students[1] (hassan) -> courses[1] (history) -> title

# 3. Get the grade of esther in her first course
print(school.students[0].courses[0].grades["Esther"])  # 95

# 4. Get the street of the third student's address
print(school.students[2].address.street)

# 5. Get the name of the department that offers the second course
target_course = school.students[0].courses[1]  # physics
# Now search departments
for dept in school.departments:
    if target_course in dept.course:
        print(dept.name)  # "Science"

# 6. Change a grade through chaining
school.students[0].courses[0].grades["Esther"] = 97
print(school.students[0].courses[0].grades["Esther"])


# 7. Get the age of the student who lives in Abuja (hassan)
for student in school.students:
    if student.address.city == "Abuja":
        print(student.age)  # 22