class StudentCount():
    StudentCount = int(input("Enter number of students:"))
    print("Number of student is:",StudentCount)

    def __init__(self,id,name,dob):
        self.id = id
        self.name = name
        self.dob = dob
    
    student = []
    listStudent = []

    for i in range(StudentCount):
        print(f"Enter student {i+1} infor:")
        id = input("Enter student ID:")
        name = input("Enter student name:")
        dob  = input("Enter student DOB:")
        student += {
            "name":name,
            "id":id,
            "dob":dob,                     
        }   
        print("ID: " + id)
        print("Name: " + name)
        print("DOB: " + dob)
        
        list = id + "/ " + name + "/ " + dob
        listStudent.append(list)
        print(listStudent)
        

class CourseCount():
    CourseCount = int(input("Enter number of course:"))
    print("Number of course is:",CourseCount)

    def __init__(this,id,name):
        this.id = id
        this.name = name
        
    course = []
    listCoures = []

    for i in range(CourseCount):
        print(f"Enter course {i+1} infor:")
        id = input("Enter course ID:")
        name = input("Enter course name:")
        listCoures.append(id)
        listCoures.append(name)
        
        print(listCoures)
        course += {
            "name":name,
            "id":id,
        }    

   