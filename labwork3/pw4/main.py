import curses
import input
import output

def main(stdscr):
    students = []
    courses = []
    marks = {} 

    curses.echo() 
    while True:
        stdscr.clear()
        stdscr.addstr("STUDENT MARK MANAGEMENT\n", curses.A_BOLD)
        stdscr.addstr("1. Input number of students and their info\n")
        stdscr.addstr("2. Input number of courses and their info\n")
        stdscr.addstr("3. Input marks for a course\n")
        stdscr.addstr("4. Calculate GPA and Sort descending\n")
        stdscr.addstr("5. List students\n")
        stdscr.addstr("6. List courses\n")
        stdscr.addstr("7. Show student marks for a given course\n")
        stdscr.addstr("8. Exit\n")
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
        elif choice == '5':
            output.list_students(stdscr, students)
        elif choice == '6':
            output.list_courses(stdscr, courses)
        elif choice == '7':
            output.show_student_marks(stdscr, students, marks)
        elif choice == '8':
            break
        else:
            stdscr.addstr("Invalid choice. Please try again.\n")
            
        stdscr.addstr("\nPress ENTER to continue...")
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)