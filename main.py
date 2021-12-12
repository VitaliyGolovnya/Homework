class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.rating:
                lecturer.rating[course] += [grade]
            else:
                lecturer.rating[course] = [grade]
        else:
            return "Ошибка"

    def avg_grades(self):
        total = 0
        length = 0
        for grade in self.grades.values():
            total += sum(grade)
            length += len(grade)
        return round(float(total / length), 2)
        
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за домашние задания: {self.avg_grades()}')
        print(f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}')
        print(f'Завершенные курсы: {", ".join(self.finished_courses)}')  

    def __lt__(self, other):
        if isinstance(other, Student):    
            if self.avg_grades() < other.avg_grades():
                return True
            else:
                return False 
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):    
            if self.avg_grades() > other.avg_grades():
                return True
            else:
                return False
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Student):    
            if self.avg_grades() <= other.avg_grades():
                return True
            else:
                return False
        else:
            return 'Ошибка' 

    def __ge__(self, other):
        if isinstance(other, Student):    
            if self.avg_grades() >= other.avg_grades():
                return True
            else:
                return False
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}
    
    def avg_rating(self):
        sum_ = 0
        length = 0
        for grade in list(self.rating.values()):
            sum_ += sum(grade)
            length += len(grade)
        res = round(sum_ / length, 2)
        return res    
        
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции: {self.avg_rating()}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):    
            if self.avg_rating() < other.avg_rating():
                return True
            else:
                return False 
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):    
            if self.avg_rating() > other.avg_rating():
                return True
            else:
                return False
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Lecturer):    
            if self.avg_rating() <= other.avg_rating():
                return True
            else:
                return False 
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Lecturer):    
            if self.avg_rating() >= other.avg_rating():
                return True
            else:
                return False
        else:
            return 'Ошибка'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')


john = Student("John", "Malkovich", "male")
john.courses_in_progress.extend(["Python", "Java", "ML"])

ellen = Student("Ellen", "Rippley", "female")
ellen.courses_in_progress.extend(["Python", "Java", "ML"])

post = Lecturer("Post", "Malone")
post.courses_attached.extend(["Python", "Java"])

kendrick = Lecturer("Kendrick", "Lamar")
kendrick.courses_attached.extend(["Java", "ML"])

fedor = Reviewer("Fedor", "Dostoevsky")
fedor.courses_attached.extend(["Python", "Java", "ML"])

lev = Reviewer("Lev", "Tolstoy")
lev.courses_attached.extend(["Python", "Java", "ML"])

john.rate_lecturer(post, "Java", 9)
john.rate_lecturer(post, "Python", 8)
john.rate_lecturer(kendrick, "Java", 10)
john.rate_lecturer(kendrick, "ML", 6)

ellen.rate_lecturer(post, "Java", 5)
ellen.rate_lecturer(post, "Python", 5)
ellen.rate_lecturer(kendrick, "Java", 5)
ellen.rate_lecturer(kendrick, "ML", 5)

fedor.rate_hw(john, "Java", 1)
fedor.rate_hw(john, "Python", 5)
fedor.rate_hw(john, "ML", 5)
fedor.rate_hw(ellen, "Python", 2)
fedor.rate_hw(ellen, "Java", 9)
fedor.rate_hw(ellen, "ML", 9)

lev.rate_hw(john, "Java", 10)
lev.rate_hw(john, "Python", 6)
lev.rate_hw(john, "ML", 3)
lev.rate_hw(ellen, "Python", 4)
lev.rate_hw(ellen, "Java", 10)
lev.rate_hw(ellen, "ML", 5)

students_list = [john, ellen]
lecturers_list = [kendrick, post]

def avg_among_students(students: list, course):
    total = 0
    length = 0
    for student in students:
        if course in student.courses_in_progress or course in student.finished_courses:
            total += sum(student.grades[course])
            length += len(student.grades[course])
        else:
            continue
    return round(total / length, 2)

def avg_among_lecturers(lecturers: list, course):
    total = 0
    length = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total += sum(lecturer.rating[course])
            length += len(lecturer.rating[course])
        else:
            continue    
    return round(total / length, 2)
