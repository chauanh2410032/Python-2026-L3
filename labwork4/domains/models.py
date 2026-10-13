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

    def set_dob(self, dob):
        self.__dob = dob
        
    def get_dob(self):
        return self.__dob

class Course(Entity):
    def __init__(self):
        super().__init__()
        self.__credits = 0 

    def input_data(self, stdscr):
        super().input_data(stdscr)
        stdscr.addstr("  Credits: ")
        stdscr.refresh()
        self.__credits = int(stdscr.getstr().decode('utf-8'))

    def get_credits(self):
        return self.__credits

    def list_info(self, stdscr):
        stdscr.addstr(f"ID: {self.get_id()} | Name: {self.get_name()} | Credits: {self.__credits}\n")