class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    @property
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
              f'Средняя оценка за домашнее задание: {self.srgr}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in\
                lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    # (в качестве аргументов принимаем список студентов и название курса)

    def avrg_estimate(self):
        total_grade = 0
        lenght = 0
        for v in self.grades.values():
            lenght += len(v)
            for el in v:
                total_grade += el
        avrg_grade = float(total_grade / lenght)
        return avrg_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr > other.srgr

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr == other.srgr


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avrg_estimate(self):
        total_grade = 0
        lenght = 0
        for v in self.grades.values():
            lenght += len(v)
            for el in v:
                total_grade += el
        avrg_grade = float(total_grade / lenght)
        return avrg_grade

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

# Перечисляем лекторов и курсы, которые они ведут
best_lecturer_1 = Lecturer('Сэнсей', 'Питонов')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Раста', 'Манов')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Гуру', 'Змееедов')
best_lecturer_3.courses_attached += ['Python']

# Перечисляем экспертов, проверяющих ДЗ
cool_rewiewer_1 = Reviewer('Джулия', 'Смотрелкина')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']

cool_rewiewer_2 = Reviewer('Венедикт', 'Кембербетчев')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']

# Перечисляем студентов, курсы, на которых они учатся, и завершенные курсы
student_1 = Student('Денис', 'Свиридов')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Роман', 'Малых')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Антонина', 'Умнова')
student_3.courses_in_progress += ['Java']
#student_3.courses_in_progress += ['Python']
student_3.finished_courses += []

# оценки за лекции от студентов
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_3.rate_hw(best_lecturer_1, 'Python', 10)

student_2.rate_hw(best_lecturer_2, 'Java', 5)
student_3.rate_hw(best_lecturer_2, 'Java', 7)

student_1.rate_hw(best_lecturer_3, 'Python', 7)
student_3.rate_hw(best_lecturer_3, 'Python', 8)

# оценки студентам за домашние задания от экспертов
cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)

cool_rewiewer_1.rate_hw(student_2, 'Java', 8)
cool_rewiewer_1.rate_hw(student_2, 'Java', 7)
cool_rewiewer_1.rate_hw(student_2, 'Java', 9)

cool_rewiewer_1.rate_hw(student_3, 'Python', 8)
cool_rewiewer_1.rate_hw(student_3, 'Python', 7)
cool_rewiewer_1.rate_hw(student_3, 'Python', 6)

cool_rewiewer_1.rate_hw(student_3, 'Java', 8)
cool_rewiewer_1.rate_hw(student_3, 'Java', 7)
cool_rewiewer_1.rate_hw(student_3, 'Java', 10)

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
print()

print('********************************')
courze = ['Java']

#print('На курсе ' + str(courze) + ' ' + student_1.name + ' ' + student_1.surname)
if student_1.courses_in_progress == courze:
    a = Student.avrg_estimate(student_1)
#    print(round(a, 1))
else:
    a = 0
#    print('не учится')

#print('На курсе ' + str(courze) + ' ' + student_2.name + ' ' + student_2.surname)
if student_2.courses_in_progress == courze:
    b = Student.avrg_estimate(student_2)
#    print(round(b, 1))
else:
    b = 0
#    print('не учится')

#print('На курсе ' + str(courze) + ' ' + student_3.name + ' ' + student_3.surname)
if student_3.courses_in_progress == courze:
    c = Student.avrg_estimate(student_3)
#    print(round(c, 1))
else:
    c = 0
#    print('не учится')

abc = round(((a + b + c) / 2), 1)
print('Средняя оценка за домашние задания по всем студентам в рамках курса Java:', abc)

courze = ['Python']

#print('На курсе ' + str(courze) + ' ' + student_1.name + ' ' + student_1.surname)
if student_1.courses_in_progress == courze:
    a = Student.avrg_estimate(student_1)
#    print(round(a, 1))
else:
    a = 0
#    print('не учится')

#print('На курсе ' + str(courze) + ' ' + student_2.name + ' ' + student_2.surname)
if student_2.courses_in_progress == courze:
    b = Student.avrg_estimate(student_2)
#    print(round(b, 1))
else:
    b = 0
#    print('не учится')

#print('На курсе ' + str(courze) + ' ' + student_3.name + ' ' + student_3.surname)
if student_3.courses_in_progress == courze:
    c = Student.avrg_estimate(student_3)
#    print(round(c, 1))
else:
    c = 0
#    print('не учится')

abc = round(((a + b + c) / 2), 1)
print('Средняя оценка за домашние задания по всем студентам в рамках курса Python:', abc)

# Препады!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print('********************************')
courze = ['Java']

if best_lecturer_1.courses_attached == courze:
    a = Lecturer.avrg_estimate(best_lecturer_1)
else:
    a = 0

if best_lecturer_2.courses_attached == courze:
    b = Lecturer.avrg_estimate(best_lecturer_2)
else:
    b = 0

if best_lecturer_3.courses_attached == courze:
    c = Lecturer.avrg_estimate(best_lecturer_3)
else:
    c = 0

abc = round(((a + b + c) / 2), 1)
print('Средняя оценка за лекции всех лекторов в рамках курса Java:', abc)

courze = ['Python']

if best_lecturer_1.courses_attached == courze:
    a = Lecturer.avrg_estimate(best_lecturer_1)
else:
    a = 0

if best_lecturer_2.courses_attached == courze:
    b = Lecturer.avrg_estimate(best_lecturer_2)
else:
    b = 0

if best_lecturer_3.courses_attached == courze:
    c = Lecturer.avrg_estimate(best_lecturer_3)
else:
    c = 0

abc = round(((a + b + c) / 2), 1)
print('Средняя оценка за лекции всех лекторов в рамках курса Python:', abc)


student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):
  count_all = []
  for stud in student_list:
    if stud.courses_in_progress == [course_name]:
      count_all.extend(stud)
  return sum(student_list.srgr()) / len(count_all)


def lecturer_rating(lecturer_list, course_name):
  sum_all = 0
  count_all = []
  for lect in lecturer_list:
    if lect.courses_attached == [course_name]:
      sum_all += len(lecturer_list[lect])
      count_all.extend(lect)
  return sum(count_all) / max(len(count_all))

# не знаю, как добиться работоспособности данного кода!

print(
  f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}"
)
print()

print(
  f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}"
)