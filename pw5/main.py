import curses
import os
import zipfile
import input
import output
from domains.models import Student, Course

def load_data(students, courses, marks):
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall(".")
            
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    s = Student()
                    s._id = parts[0]
                    s._name = parts[1]
                    s.set_dob(parts[2])
                    if len(parts) == 4:
                        s.set_gpa(float(parts[3]))
                    students.append(s)
                    
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    c = Course()
                    c._id = parts[0]
                    c._name = parts[1]
                    c._Course__credits = int(parts[2]) 
                    courses.append(c)
                    marks[c.get_id()] = {}
                    
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id][s_id] = mark

def compress_data():
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        if os.path.exists("students.txt"): zipf.write("students.txt")
        if os.path.exists("courses.txt"): zipf.write("courses.txt")
        if os.path.exists("marks.txt"): zipf.write("marks.txt")

def main(stdscr):
    students = []
    courses = []
    marks = {} 
    load_data(students, courses, marks)
    curses.echo() 
    while True:
        stdscr.clear()
        stdscr.addstr("STUDENT MARK MANAGEMENT (Persistent Info)\n", curses.A_BOLD)
        stdscr.addstr("1. Input number of students and their info\n")
        stdscr.addstr("2. Input number of courses and their info\n")
        stdscr.addstr("3. Input marks for a course\n")
        stdscr.addstr("4. Calculate GPA and Sort descending\n")
        stdscr.addstr("5. List students\n")
        stdscr.addstr("6. List courses\n")
        stdscr.addstr("7. Show student marks for a given course\n")
        stdscr.addstr("8. Exit (and Compress Data)\n")
        stdscr.addstr("Select an option: ")
        stdscr.refresh()
        choice = stdscr.getstr().decode('utf-8')
        stdscr.clear()
        
        if choice == '1':
            input.input_students(stdscr, students)
        elif choice == '2':
            input.input_courses(stdscr, courses, marks)
        elif choice == '3':
            input.input_marks(stdscr, courses, students, marks)
        elif choice == '4':
            output.calculate_and_sort_gpa(stdscr, students, courses, marks)
            with open("students.txt", "w") as f:
                for s in students:
                    f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()},{s.get_gpa()}\n")
        elif choice == '5':
            output.list_students(stdscr, students)
        elif choice == '6':
            output.list_courses(stdscr, courses)
        elif choice == '7':
            output.show_student_marks(stdscr, students, marks)
        elif choice == '8':
            compress_data() 
            break
        else:
            stdscr.addstr("Invalid choice. Please try again.\n")
            
        stdscr.addstr("\nPress ENTER to continue...")
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)