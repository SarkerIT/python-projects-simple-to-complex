# school management system
class Campus_people:
    def __init__(self, first, last, year_started) -> None:
        self.first = first
        self.last = last
        self.year_admit = year_started

    def full_name(self):
        print(f"{self.first} {self.last}")

    def email(self):
        print(f"{self.first.lower()}.{self.last.lower()}@youremail.com")


class Student(Campus_people):
    def __init__(self, first, last, year_started, major) -> None:
        super().__init__(first, last, year_started)
        self.major = major

    def total_score(self, score):
        self.score = score
        print(f"Your total points: {self.score}")

    def score_with_extra_credit(self, score):
        extra_cr = 1.05
        credit_with_ex_credit = score * extra_cr
        print(f"Total points with extra credit: {credit_with_ex_credit}")


class Professor(Campus_people):
    def __init__(self, first, last, year_started, subject_teach, do_esearch) -> None:
        super().__init__(first, last, year_started)
        self.subject_teach = subject_teach
        self.do_research = do_esearch


## DRIVER Code
# for student
print("\n")
student_1 = Student("Rocky", "Pythony", 2020, "Computer engineering")
student_1.full_name()
student_1.email()
# student_1.major()  # will not work; not a method but an attribute
# print(student_1.major()) # will not work not a method

print(student_1.major)

# For Professor
print("\n")
prof_1 = Professor("John", "Smith", 2020, "Phychology", "False")

prof_1.email()
print(prof_1.subject_teach)
print(prof_1.do_research)
