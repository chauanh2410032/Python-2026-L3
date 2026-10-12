import numpy as np

def calculate_and_sort_gpa(stdscr, students, courses, marks):
    for student in students:
        s_id = student.get_id()
        student_marks = []
        student_credits = []
        
        for course in courses:
            c_id = course.get_id()
            if c_id in marks and s_id in marks[c_id]:
                student_marks.append(marks[c_id][s_id])
                student_credits.append(course.get_credits())
        
        if student_marks:
            arr_marks = np.array(student_marks)
            arr_credits = np.array(student_credits)
            gpa = np.sum(arr_marks * arr_credits) / np.sum(arr_credits)
            student.set_gpa(gpa)
        else:
            student.set_gpa(0.0)

    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    stdscr.addstr("GPA calculated and students sorted descendingly!\n")

def list_students(stdscr, students):
    stdscr.addstr("\nList Students (Sorted by GPA if calculated)\n")
    if not students:
        stdscr.addstr("Empty.\n")
    else:
        for student in students:
            student.list_info(stdscr)

def list_courses(stdscr, courses):
    stdscr.addstr("\nList Courses\n")
    if not courses:
        stdscr.addstr("Empty.\n")
    else:
        for course in courses:
            course.list_info(stdscr)

def show_student_marks(stdscr, students, marks):
    stdscr.addstr("Course ID to show marks: ")
    stdscr.refresh()
    c_id = stdscr.getstr().decode('utf-8')
    
    if c_id not in marks:
        stdscr.addstr("Course not found\n")
        return

    stdscr.addstr(f"\nMark for course: {c_id}\n")
    if not marks[c_id]:
        stdscr.addstr("No marks have been inputted for this course yet.\n")
    else:
        for student in students:
            s_id = student.get_id()
            if s_id in marks[c_id]:
                stdscr.addstr(f"Student: {student.get_name()} - Mark: {marks[c_id][s_id]}\n")
            else:
                stdscr.addstr(f"Student: {student.get_name()} - Mark: None\n")