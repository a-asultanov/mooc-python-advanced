# tee ratkaisusi tänne

class Course:
    def __init__(self):
        self.__course_name = None
        self.__course_grade = None
        self.__course_credits = None

    @property
    def name(self):
        name = self.__course_name
        return name

    @property
    def grade(self):
        grade = self.__course_grade
        return grade

    @property
    def credits(self):
        credits = self.__course_credits
        return credits

    def print_data(self):
        print(f"{self.name} ({self.credits} cr) grade {self.grade}")

    def add_course_name(self, name: str):
        self.__course_name = name
    
    def add_course_grade(self, grade: int):
        self.__course_grade = grade

    def add_course_credits(self, credits):
        self.__course_credits = credits

class CourseRecords:
    def __init__(self):
        self.courses = {}

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        course_name = name.lower()
        
        if not course_name in self.courses:
            grades= []
            credits = []
            grades.append(grade)
            credits.append(credit)
            self.courses[course_name] = grades, credits
        else:
            self.courses[course_name][0].append(grade)
            self.courses[course_name][1].append(credit)


    def get_course_data(self):
        name = input("course: ")
        name_lower = name.lower()
        if name_lower not in self.courses:
            print("no entry for this course")
            return
        grades = self.courses[name_lower][0]
        credits = self.courses[name_lower][1]
        recent_grade = max(grades)
        recent_credit = max(credits)

        print(f"course: {name}\n{name} ({recent_credit} cr) grade {recent_grade}")

    def statistics(self):
        total_credits = 0
        total_grades = 0 
        for course_name in self.courses:
            credit_list = self.courses[course_name][1]
            grades_list = self.courses[course_name][0]
            max_grade = max(grades_list)
            total_grades += max_grade
            first_credits = credit_list[0]
            total_credits += first_credits
            
        
        completed_courses = len(self.courses)
        mean = total_grades / completed_courses
        print(f"{completed_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        grade_count = {}
        for course_name in self.courses: 
            grades_list = self.courses[course_name][0]
            max_grade = max(grades_list)
            if max_grade in grade_count:
                grade_count[max_grade] += 1
            else:
                grade_count[max_grade] = 1

        for grade in range(5, 0, -1):
            count = grade_count.get(grade, 0)
            print(f"{grade}: {'x' * count}")
            
records = CourseRecords()
while True:
    print("command: ")
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")
    command = input()

    if command == "0":
        break

    elif command == "1":
        records.add_course()

    elif command == "2":        
        records.get_course_data()

    elif command == "3":
        records.statistics()
    
