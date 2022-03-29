class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_mark(self, course, mark):
        self.marks.update({course: mark})

    def displayStudent(self):
        print("Student ID: " + self.id)
        print("Student name: " + self.name)
        print("Student DoB: " + self.dob)
        print("-------")

    def displayMark(self, course):
        print(self.name + "'s mark: " + str(self.marks.get(course)))


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def displayCourse(self):
        print("Course ID: " + self.id)
        print("Course name: " + self.name)
        


def numOfStudent():
    while True:
        try:
            studentnumber = int(input("Enter number of student in the class: "))          
            return studentnumber
        except ValueError:
            print("Enter again")


def studentInfo():
    studentid = input("Enter student ID: ")
    studentname = input("Enter student name: ")
    studentdob = input("Enter student DOB: ")
    
    return studentid,studentname,studentdob


def numOfCourse():
    while True:
        try:
            coursenumber = int(input("Enter number of courses: "))           
            return coursenumber
        except ValueError:
            print("Enter again")


def courseInfo():
    courseid = input("Enter course ID: ")
    coursename = input("Enter course name: ")
    
    return courseid, coursename


def findCourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Err: Invalid ID")


if __name__ == "__main__":
    students = []
    courses = []

    student_num = numOfStudent()
    print(student_num)
    for i in range(student_num):
        id, name, dob = studentInfo()
        students.append(Student(id, name, dob))

    course_num = numOfCourse()
    for i in range(course_num):
        id, name = courseInfo()
        courses.append(Course(id, name))

    print("Students information:\n")
    for student in students:
        student.displayStudent()

    print("Courses information:\n")
    for course in courses:
        course.displayCourse()

    