import math
import numpy as np
import curses

class Entity:
    def __init__(self):
        self._id = ""
        self._name = ""

    def input_data(self, stdscr):
        stdscr.addstr("  ID: ")
        stdscr.refresh()
        self._id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Name: ")
        stdscr.refresh()
        self._name = stdscr.getstr().decode('utf-8')

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

class Student(Entity):
    def __init__(self):
        super().__init__()
        self.__dob = ""
        self.__gpa = 0.0 

    def input_data(self, stdscr):
        super().input_data(stdscr)
        stdscr.addstr("  Date of Birth: ")
        stdscr.refresh()
        self.__dob = stdscr.getstr().decode('utf-8')

    def set_gpa(self, gpa):
        self.__gpa = gpa
        
    def get_gpa(self):
        return self.__gpa

    def list_info(self, stdscr):
        stdscr.addstr(f"ID: {self.get_id()} | Name: {self.get_name()} | DoB: {self.__dob} | GPA: {self.__gpa:.2f}\n")

class Course(Entity):
    def __init__(self):
        super().__init__()
        self.__credits = 0 

    def input_data(self, stdscr):
        super().input_data(stdscr)
        stdscr.addstr("  Credits (Trọng số tín chỉ): ")
        stdscr.refresh()
        self.__credits = int(stdscr.getstr().decode('utf-8'))

    def get_credits(self):
        return self.__credits

    def list_info(self, stdscr):
        stdscr.addstr(f"ID: {self.get_id()} | Name: {self.get_name()} | Credits: {self.__credits}\n")

class MarkManagement:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.__students = []
        self.__courses = []
        self.__marks = {} 

    def input_students(self):
        self.stdscr.addstr("Number of students in the class: ")
        self.stdscr.refresh()
        num = int(self.stdscr.getstr().decode('utf-8'))
        
        for i in range(num):
            self.stdscr.addstr(f"\nStudent {i+1}:\n")
            student = Student()
            student.input_data(self.stdscr)
            self.__students.append(student)

    def input_courses(self):
        self.stdscr.addstr("Number of courses: ")
        self.stdscr.refresh()
        num = int(self.stdscr.getstr().decode('utf-8'))
        
        for i in range(num):
            self.stdscr.addstr(f"\nCourse {i+1}:\n")
            course = Course()
            course.input_data(self.stdscr)
            self.__courses.append(course)
            self.__marks[course.get_id()] = {} 

    def input_marks(self):
        if not self.__courses:
            self.stdscr.addstr("No courses available\n")
            return
        
        self.stdscr.addstr("Course ID to input marks: ")
        self.stdscr.refresh()
        c_id = self.stdscr.getstr().decode('utf-8')
        
        if c_id not in [c.get_id() for c in self.__courses]:
            self.stdscr.addstr("Course not found!\n")
            return

        self.stdscr.addstr("Marks for students in this course:\n")
        for student in self.__students:
            self.stdscr.addstr(f"  Mark for {student.get_name()} (ID: {student.get_id()}): ")
            self.stdscr.refresh()
            raw_mark = float(self.stdscr.getstr().decode('utf-8'))
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            self.__marks[c_id][student.get_id()] = rounded_mark

    def calculate_and_sort_gpa(self):
        for student in self.__students:
            s_id = student.get_id()
            student_marks = []
            student_credits = []
            
            for course in self.__courses:
                c_id = course.get_id()
                if c_id in self.__marks and s_id in self.__marks[c_id]:
                    student_marks.append(self.__marks[c_id][s_id])
                    student_credits.append(course.get_credits())
            
            if student_marks:
                arr_marks = np.array(student_marks)
                arr_credits = np.array(student_credits)
                gpa = np.sum(arr_marks * arr_credits) / np.sum(arr_credits)
                student.set_gpa(gpa)
            else:
                student.set_gpa(0.0)

        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)
        self.stdscr.addstr("GPA calculated and students sorted descendingly!\n")

    def list_students(self):
        self.stdscr.addstr("\nList Students (Sorted by GPA if calculated)\n")
        if not self.__students:
            self.stdscr.addstr("Empty.\n")
        else:
            for student in self.__students:
                student.list_info(self.stdscr)

    def list_courses(self):
        self.stdscr.addstr("\nList Courses\n")
        if not self.__courses:
            self.stdscr.addstr("Empty.\n")
        else:
            for course in self.__courses:
                course.list_info(self.stdscr)

    def show_student_marks(self):
        self.stdscr.addstr("Course ID to show marks: ")
        self.stdscr.refresh()
        c_id = self.stdscr.getstr().decode('utf-8')
        
        if c_id not in self.__marks:
            self.stdscr.addstr("Course not found\n")
            return

        self.stdscr.addstr(f"\nMark for course: {c_id}\n")
        if not self.__marks[c_id]:
            self.stdscr.addstr("No marks have been inputted for this course yet.\n")
        else:
            for student in self.__students:
                s_id = student.get_id()
                if s_id in self.__marks[c_id]:
                    self.stdscr.addstr(f"Student: {student.get_name()} - Mark: {self.__marks[c_id][s_id]}\n")
                else:
                    self.stdscr.addstr(f"Student: {student.get_name()} - Mark: None\n")

    def run(self):
        curses.echo() 
        while True:
            self.stdscr.clear()
            self.stdscr.addstr("STUDENT MARK MANAGEMENT\n", curses.A_BOLD)
            self.stdscr.addstr("1. Input number of students and their info\n")
            self.stdscr.addstr("2. Input number of courses and their info\n")
            self.stdscr.addstr("3. Input marks for a course (Math floor applied)\n")
            self.stdscr.addstr("4. Calculate GPA (Numpy) and Sort descending\n")
            self.stdscr.addstr("5. List students\n")
            self.stdscr.addstr("6. List courses\n")
            self.stdscr.addstr("7. Show student marks for a given course\n")
            self.stdscr.addstr("8. Exit\n")
            self.stdscr.addstr("Select an option: ")
            self.stdscr.refresh()
            choice = self.stdscr.getstr().decode('utf-8')
            self.stdscr.clear()
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.calculate_and_sort_gpa()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.list_courses()
            elif choice == '7':
                self.show_student_marks()
            elif choice == '8':
                break
            else:
                self.stdscr.addstr("Invalid choice. Please try again.\n")
            self.stdscr.addstr("\nPress ENTER to continue...")
            self.stdscr.getch()

def main(stdscr):
    app = MarkManagement(stdscr)
    app.run()

if __name__ == "__main__":
    curses.wrapper(main)