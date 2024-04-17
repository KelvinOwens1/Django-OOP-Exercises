class AttendanceTracker:
    def __init__(self) -> None:
        self.students = {}

    def add_student(self, student):
        if student in self.students.keys():
            raise ValueError(f"student")
        else:
            self.students[student] = [student, False]

    def check_in(self, student):
        if student not in self.students.keys():
            raise ValueError("Students not Found")
        self.students[student] = [student, True]

    def delete_student(self, student):
        if student not in self.students.keys():
            raise ValueError("Student not in list")
        del self.students[student]





    

# std_1 = AttendanceTracker("John")

# print(std_1)