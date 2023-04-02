class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def srgr(self):
        if not self.grades:
            return 0
        spisok = []
        for k in self.grades.values():
            spisok.extend(k)
        return round(sum(spisok) / len(spisok), 2)

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.srgr()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer
        ) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() > other.srgr()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() == other.srgr()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def srgr(self):
        if not self.grades:
            return 0
        spisok = []
        for k in self.grades.values():
            spisok.extend(k)
        return round(sum(spisok) / len(spisok), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr() > other.srgr()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr() == other.srgr()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_lecturer_1 = Lecturer('Сэнсей', 'Питонов')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Раста', 'Манов')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Гуру', 'Змееедов')
best_lecturer_3.courses_attached += ['Python']

cool_rewiewer_1 = Reviewer('Джулия', 'Смотрелкина')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']

cool_rewiewer_2 = Reviewer('Венедикт', 'Кембербетчев')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']

student_1 = Student('Денис', 'Свиридов')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Роман', 'Малых')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Антонина', 'Умнова')
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Git']
student_3.finished_courses += []

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Java', 5)
student_1.rate_hw(best_lecturer_2, 'Java', 7)
student_1.rate_hw(best_lecturer_2, 'Java', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 5)
student_2.rate_hw(best_lecturer_2, 'Java', 6)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)

cool_rewiewer_2.rate_hw(student_2, 'Java', 8)
cool_rewiewer_2.rate_hw(student_2, 'Java', 7)
cool_rewiewer_2.rate_hw(student_2, 'Java', 9)

cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)

print(
    f'Перечень проверяющих:\n\n{cool_rewiewer_1}\n\n{cool_rewiewer_2}'
)
print()
print()

print('********************************')
print(
    f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}'
)
print()
print()

print('********************************')
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Реализация возможности сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
# и студентов по средней оценке за домашние задания

print('********************************')
print('Cравнение между собой лекторов по средней оценке за лекции:')

l1 = best_lecturer_1.__lt__(best_lecturer_2)
l2 = best_lecturer_1.__le__(best_lecturer_2)
l3 = best_lecturer_1.__eq__(best_lecturer_2)

l4 = best_lecturer_2.__lt__(best_lecturer_3)
l5 = best_lecturer_2.__le__(best_lecturer_3)
l6 = best_lecturer_2.__eq__(best_lecturer_3)

l7 = best_lecturer_3.__lt__(best_lecturer_1)
l8 = best_lecturer_3.__le__(best_lecturer_1)
l9 = best_lecturer_3.__eq__(best_lecturer_1)

if l1:
    print(
        best_lecturer_1.name + ' ' + best_lecturer_1.surname + ' < ' +
        best_lecturer_2.name + ' ' + best_lecturer_2.surname)
elif l2:
    print(
        best_lecturer_1.name + ' ' + best_lecturer_1.surname + ' > ' +
        best_lecturer_2.name + ' ' + best_lecturer_2.surname)
else:
    print(
        best_lecturer_1.name + ' ' + best_lecturer_1.surname + ' = ' +
        best_lecturer_2.name + ' ' + best_lecturer_2.surname)

if l4:
    print(
        best_lecturer_2.name + ' ' + best_lecturer_2.surname + ' < ' +
        best_lecturer_3.name + ' ' + best_lecturer_3.surname)
elif l5:
    print(
        best_lecturer_2.name + ' ' + best_lecturer_2.surname + ' > ' +
        best_lecturer_3.name + ' ' + best_lecturer_3.surname)
else:
    print(
        best_lecturer_2.name + ' ' + best_lecturer_2.surname + ' = ' +
        best_lecturer_3.name + ' ' + best_lecturer_3.surname)

if l7:
    print(
        best_lecturer_3.name + ' ' + best_lecturer_3.surname + ' < ' +
        best_lecturer_1.name + ' ' + best_lecturer_1.surname)
elif l8:
    print(
        best_lecturer_3.name + ' ' + best_lecturer_3.surname + ' > ' +
        best_lecturer_1.name + ' ' + best_lecturer_1.surname)
else:
    print(
        best_lecturer_3.name + ' ' + best_lecturer_3.surname + ' = ' +
        best_lecturer_1.name + ' ' + best_lecturer_1.surname)

print()

print('********************************')
print('Сравнение студентов по средней оценке за домашние задания:')

s1 = student_1.__lt__(student_2)
s2 = student_1.__le__(student_2)
s3 = student_1.__eq__(student_2)

s4 = student_2.__lt__(student_3)
s5 = student_2.__le__(student_3)
s6 = student_2.__eq__(student_3)

s7 = student_3.__lt__(student_1)
s8 = student_3.__le__(student_1)
s9 = student_3.__eq__(student_1)

if s1:
    print(student_1.name + ' ' + student_1.surname + ' < ' + student_2.name + ' ' + student_2.surname)
elif s2:
    print(student_1.name + ' ' + student_1.surname + ' > ' + student_2.name + ' ' + student_2.surname)
else:
    print(student_1.name + ' ' + student_1.surname + ' = ' + student_2.name + ' ' + student_2.surname)

if s4:
    print(student_2.name + ' ' + student_2.surname + ' < ' + student_3.name + ' ' + student_3.surname)
elif s5:
    print(student_2.name + ' ' + student_2.surname + ' > ' + student_3.name + ' ' + student_3.surname)
else:
    print(student_2.name + ' ' + student_2.surname + ' = ' + student_3.name + ' ' + student_3.surname)

if s7:
    print(student_3.name + ' ' + student_3.surname + ' < ' + student_1.name + ' ' + student_1.surname)
elif s8:
    print(student_3.name + ' ' + student_3.surname + ' > ' + student_1.name + ' ' + student_1.surname)
else:
    print(student_3.name + ' ' + student_3.surname + ' = ' + student_1.name + ' ' + student_1.surname)
