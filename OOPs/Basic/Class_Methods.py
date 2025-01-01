class Student:
    # attributes
    rollNo: int # self.rollNo
    name: str
    grade: int

    #Methods - instance methods
    def scan_student(self, rollNo: int, name: str, grade: int) -> None:
        self.rollNo = rollNo
        self.name = name
        self.grade = grade

    def print_student(self) -> None:
        print(f"\nRollNo: {self.rollNo}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

# main module
if __name__ == "__main__":
    s = Student()
    s.scan_student(101, "Kaushal", 1)
    s.print_student()
    s.marks = 34
    print(f"Marks: {s.marks}")