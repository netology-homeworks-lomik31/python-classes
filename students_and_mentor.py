class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}"

    def avg_grade(self):
        if (len(self.grades) == 0): return 0
        grades = sum(map(lambda i: i, self.grades.values()), [])
        return f"{sum(grades)/len(grades):.1f}"

    def __gt__(self, other):
        if (not isinstance(other, type(self))): raise TypeError("Unsupported operator")
        return float(self.avg_grade()) > float(other.avg_grade())


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\n\
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __gt__(self, other):
        if (not isinstance(other, type(self))): raise TypeError("Unsupported operator")
        return float(self.avg_grade()) > float(other.avg_grade())

    def rate_hw(self, lecturer: Lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and isinstance(grade, int) and grade > 0 and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        if (len(self.grades) == 0): return 0
        grades = sum(map(lambda i: i, self.grades.values()), [])
        return f"{sum(grades)/len(grades):.1f}"

   
class Reviewer(Mentor):
    def rate_hw(self, student: Student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and isinstance(grade, int) and grade > 0 and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Program:
    def avg_students(self, students: list, course_name: str):
        grades = []
        for i in students:
            if (not isinstance(i, Student)): raise TypeError("Список СТУДЕНТОВ а")
            if (course_name not in i.grades): pass
            grades += i.grades[course_name]
        return f"{sum(grades)/len(grades):.1f}"
    
    def avg_lecturers(self, lecturers: list, course_name: str):
        grades = []
        for i in lecturers:
            if (not isinstance(i, Lecturer)): raise TypeError("Список ЛЕКТОРОВ а")
            if (course_name not in i.grades): pass
            grades += i.grades[course_name]
        return f"{sum(grades)/len(grades):.1f}"

    def Main(self):
        s1 = Student("test1", "", None)
        s2 = Student("test2", "", None)
        s1.courses_in_progress.append("amogus")
        s2.courses_in_progress.append("amogus")
        l1 = Lecturer("test3", "")
        l2 = Lecturer("test4", "")
        l1.courses_attached.append("amogus")
        l2.courses_attached.append("amogus")
        s1.rate_hw(l1, "amogus", 8)
        s2.rate_hw(l2, "amogus", 7)
        s1.rate_hw(l1, "amogus", 5)
        s2.rate_hw(l2, "amogus", 3)
        r1 = Reviewer("test5", "")
        r2 = Reviewer("test6", "")
        r1.courses_attached.append("amogus")
        r1.rate_hw(s1, "amogus", 9)
        r1.rate_hw(s2, "amogus", 7)
        print(s1 < s2)
        print(l1 > l2)
        print("", s1, l2, r1, sep="\n\n")
        print("", self.avg_students([s1, s2], "amogus"), self.avg_lecturers([l1, l2], "amogus"), sep="\n\n")


if __name__ == "__main__":
    program = Program()
    program.Main()