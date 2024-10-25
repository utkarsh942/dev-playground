class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self, roll_no, name, age, grade):
        """
        Bug: Function doesn't properly check for duplicate roll numbers
        It compares strings instead of integers for roll numbers
        """
        # Bug: Incorrect string comparison instead of integer comparison
        if any(int(student.roll_no) == int(roll_no) for student in self.students):
            return False, "Roll number already exists"
        
        new_student = Student(roll_no, name, age, grade)
        self.students.append(new_student)
        return True, "Student added successfully"
    
    def get_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None
    
    def display_all_students(self):
        if not self.students:
            return "No students registered"
        
        result = "Student List:\n"
        for student in self.students:
            result += f"Roll No: {student.roll_no}, Name: {student.name}, "
            result += f"Age: {student.age}, Grade: {student.grade}\n"
        return result

# Usage Example
if __name__ == "__main__":
    sms = StudentManagementSystem()
    
    # These additions will work even though they should be duplicates
    sms.add_student("001", "John Doe", 18, "A")
    sms.add_student(1, "Jane Smith", 19, "B")

    
    print(sms.display_all_students())
