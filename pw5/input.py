import math
from domains.models import Student, Course

def input_students(stdscr, students):
    stdscr.addstr("Number of students in the class: ")
    stdscr.refresh()
    num = int(stdscr.getstr().decode('utf-8'))
    
    for i in range(num):
        stdscr.addstr(f"\nStudent {i+1}:\n")
        student = Student()
        student.input_data(stdscr)
        students.append(student)
        
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()},{s.get_gpa()}\n")

def input_courses(stdscr, courses, marks):
    stdscr.addstr("Number of courses: ")
    stdscr.refresh()
    num = int(stdscr.getstr().decode('utf-8'))
    
    for i in range(num):
        stdscr.addstr(f"\nCourse {i+1}:\n")
        course = Course()
        course.input_data(stdscr)
        courses.append(course)
        marks[course.get_id()] = {}
        
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

def input_marks(stdscr, courses, students, marks):
    if not courses:
        stdscr.addstr("No courses available\n")
        return
    
    stdscr.addstr("Course ID to input marks: ")
    stdscr.refresh()
    c_id = stdscr.getstr().decode('utf-8')
    
    if c_id not in [c.get_id() for c in courses]:
        stdscr.addstr("Course not found!\n")
        return

    stdscr.addstr("Marks for students in this course:\n")
    for student in students:
        stdscr.addstr(f"  Mark for {student.get_name()} (ID: {student.get_id()}): ")
        stdscr.refresh()
        raw_mark = float(stdscr.getstr().decode('utf-8'))
        rounded_mark = math.floor(raw_mark * 10) / 10.0
        marks[c_id][student.get_id()] = rounded_mark
        
    with open("marks.txt", "w") as f:
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                f.write(f"{course_id},{student_id},{mark}\n")