class Entity:
    def __init__(self):
        self._id = ""
        self._name = ""

    def input(self):
        self._id = input("  ID: ")
        self._name = input("  Name: ")

    def list(self):
        pass

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

class Student(Entity):
    def __init__(self):
        super().__init__() 
        self.__dob = ""

    def input(self):
        super().input() 
        self.__dob = input("  Date of Birth: ")

    def list(self):
        print(f"ID: {self.get_id()} | Name: {self.get_name()} | DoB: {self.__dob}")

class Course(Entity):
    def __init__(self):
        super().__init__()

    def list(self):
        print(f"ID: {self.get_id()} | Name: {self.get_name()}")

class MarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {} # format: { course_id: { student_id: mark } }

    def input_students(self):
        num = int(input("Number of students in the class: "))
        for i in range(num):
            print(f"\nStudent {i+1}:")
            student = Student()
            student.input() 
            self.__students.append(student)

    def input_courses(self):
        num = int(input("Number of courses: "))
        for i in range(num):
            print(f"\nCourse {i+1}:")
            course = Course()
            course.input() 
            self.__courses.append(course)
            self.__marks[course.get_id()] = {} 

    def input_marks(self):
        if not self.__courses:
            print("No courses available")
            return
        
        c_id = input("Course ID to input marks: ")
        
        if c_id not in [c.get_id() for c in self.__courses]:
            print("Course not found!")
            return

        print("Marks for students in this course:")
        for student in self.__students:
            mark = float(input(f"  Mark for {student.get_name()} (ID: {student.get_id()}): "))
            self.__marks[c_id][student.get_id()] = mark

    def list_students(self):
        print("\nList Students")
        if not self.__students:
            print("Empty.")
        else:
            for student in self.__students:
                student.list() 

    def list_courses(self):
        print("\nList Courses")
        if not self.__courses:
            print("Empty.")
        else:
            for course in self.__courses:
                course.list() 

    def show_student_marks(self):
        c_id = input("Course ID to show marks: ")
        
        if c_id not in self.__marks:
            print("Course not found")
            return

        print(f"\nMark for course: {c_id} ")
        if not self.__marks[c_id]:
            print("No marks have been inputted for this course yet.")
        else:
            for student in self.__students:
                s_id = student.get_id()
                if s_id in self.__marks[c_id]:
                    print(f"Student: {student.get_name()} - Mark: {self.__marks[c_id][s_id]}")
                else:
                    print(f"Student: {student.get_name()} - Mark: None")

    def run(self):
        while True:
            print("\nSTUDENT MARK MANAGEMENT")
            print("1. Input number of students and their info")
            print("2. Input number of courses and their info")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show student marks for a given course")
            print("7. Exit")
            
            choice = input("Select an option (1-7): ")
            
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_students()
            elif choice == '5':
                self.list_courses()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '7':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = MarkManagement()
    app.run()