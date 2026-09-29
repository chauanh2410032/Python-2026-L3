students = []
courses = []
marks = {}

def input_students():
    num = int(input("Number of students in the class: "))
    for i in range(num):
        print(f"\nStudent {i+1}:")
        s_id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  Date of Birth: ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    num = int(input("Number of courses: "))
    for i in range(num):
        print(f"\nCourse {i+1}:")
        c_id = input("  ID: ")
        name = input("  Name: ")
        courses.append({"id": c_id, "name": name})
        marks[c_id] = {}

def input_marks():
    if not courses:
        print("No courses available")
        return
    
    c_id = input("Course ID to input marks: ")

    course_exists = False
    for c in courses:
        if c['id'] == c_id:
            course_exists = True
            break
            
    if not course_exists:
        print("Course not found!")
        return

    print("Marks for students in this course:")
    for s in students:
        mark = float(input(f"  Mark for {s['name']} (ID: {s['id']}): "))
        marks[c_id][s['id']] = mark

def list_students():
    print("\nList Students")
    if not students:
        print("Empty.")
    else:
        for s in students:
            print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def list_courses():
    print("\nList Courses")
    if not courses:
        print("Empty.")
    else:
        for c in courses:
            print(f"ID: {c['id']} | Name: {c['name']}")

def show_student_marks():
    c_id = input("Course ID to show marks: ")
    
    if c_id not in marks:
        print("Course not found")
        return

    print(f"\nMark for courses: {c_id} ")
    if not marks[c_id]:
        print("No marks have been inputted for this course yet.")
    else:
        for s in students:
            s_id = s['id']
            if s_id in marks[c_id]:
                print(f"Student: {s['name']} - Mark: {marks[c_id][s_id]}")
            else:
                print(f"Student: {s['name']} - Mark: None")

def main():
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
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()