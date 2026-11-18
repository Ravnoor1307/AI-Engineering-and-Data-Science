"""
##  Smart Student Management System

[Microsoft Power BI Consulting Services | Data-Driven Insights – Comfygen](https://images.openai.com/static-rsc-4/PpY5noc-f2Iynax7LKgQAfC3wKj3lLuGZs9STPAC6gnhHUgrE7Kp4G_Jib_XrYpNcvHiEwigjBD1KuhB3IMw9mhsXENRtq9661Zsc8eX3V6nIvm6u4lA-nfspYtvUAVxJFhyvvjm6YE3wXWiFcAILNoppWOsbbcawzxYV7yXedY?purpose=inline)

[comfygen.com](https://www.comfygen.com/data/power-bi-consulting-services?utm_source=chatgpt.com)

Scenario:

Your college wants a small Python application to manage student records. The application should store students, their marks, and their attendance.

Your tasks:

1. Take the names of 5 students as input.
2. Store their names and marks using an appropriate Python collection.
3. Calculate the average marks of each student.
4. Identify students who scored more than 80.
5. Find the student with the highest marks.
6. Remove duplicate student names.
7. Sort students according to their marks in descending order.
8. Display students who have attendance below 75%.
9. Create a function that accepts student information and returns their result status:
   - 90 or above: Excellent
   - 75–89: Very Good
   - 50–74: Pass
   - Below 50: Fail

Concepts being tested: Lists, dictionaries, sets, tuples, loops, conditions, functions, sorting, type conversion, and list comprehension.


## Rules for your practice

1. First understand the problem.
2. Identify the required data types.
3. Decide which functions or classes are needed.
4. Write the logic yourself.
5. Test with different inputs and edge cases.
6. Follow PEP 8.
7. Avoid copying solutions from the internet.



"""


import os


class Student:

    def __init__(self,name=None, marks=None, attendance=None):
        self.name = name
        self.marks = marks if marks is not None else []
        self.attendance = attendance
        self.students = {}

    def __str__(self):
        return f"Name: {self.name},\nMarks: {sum(self.marks)/len(self.marks):.2f}, \nAttendance: {self.attendance}%"

    def __menu(self):
        while True:
            self.__clear_Screen()
            print("Student Management System.")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Calculate Average Marks")
            print("4. Identify Students with Marks > 80")
            print("5. Find Student with Highest Marks")
            print("6. Remove Duplicate Student Names")
            print("7. Sort Students by Marks (Descending)")
            print("8. Display Students with Attendance < 75%")
            print("9. Get Result Status of a Student")
            print("10. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please enter a number from 1 to 10.")
                input("Press Enter to continue...")
                continue

            actions = {
                1: self.__add_student,
                2: self.__display_students,
                3: self.__calculate_average_marks,
                4: self.__identify_students_above_80,
                5: self.__find_student_with_highest_marks,
                6: self.__remove_duplicate_student_names,
                7: self.__sort_students_by_marks,
                8: self.__display_students_with_low_attendance,
                9: self.__get_result_status,
            }
            if choice == 10:
                self.__clear_Screen()
                print("Exiting...")
                return
            action = actions.get(choice)
            if action is None:
                print("Invalid choice. Please try again.")
            else:
                self.__clear_Screen()
                action()
            input("Press Enter to continue...")

    def __add_student(self):
        name = input("Enter student name: ")
        marks = list(map(float, input("Enter marks separated by space: ").split()))
        attendance = float(input("Enter attendance percentage: "))
        self.__clear_Screen()
        student = Student(name, marks, attendance)
        self.students[name] = student
        print("Student added successfully.")


    def __display_students(self):
        if not self.students:
            print("No students to display.")
            return
        for student in self.students.values():
            print(student)

    def __calculate_average_marks(self):
        if not self.students:
            print("No students to calculate average marks.")
            return
        for student in self.students.values():
            average_marks = sum(student.marks) / len(student.marks)
            print(f"{student.name}: Average Marks = {average_marks:.2f}")

    def __identify_students_above_80(self):
        if not self.students:
            print("No students to identify.")
            return
        for student in self.students.values():
            average_marks = sum(student.marks) / len(student.marks)
            if average_marks > 80:
                print(f"{student.name}: Average Marks = {average_marks:.2f}")

    def __find_student_with_highest_marks(self):
        if not self.students:
            print("No students to find.")
            return
        highest_student = max(self.students.values(), key=lambda s: sum(s.marks) / len(s.marks))
        average_marks = sum(highest_student.marks) / len(highest_student.marks)
        print(f"Student with highest marks: {highest_student.name}, Average Marks = {average_marks:.2f}")

    def __remove_duplicate_student_names(self):
        if not self.students:
            print("No students to remove duplicates.")
            return
        unique_students = {}
        for name, student in self.students.items():
            if name not in unique_students:
                unique_students[name] = student
        self.students = unique_students
        print("Duplicate student names removed.")

    def __sort_students_by_marks(self):
        if not self.students:
            print("No students to sort.")
            return
        sorted_students = sorted(self.students.values(), key=lambda s: sum(s.marks) / len(s.marks), reverse=True)
        for student in sorted_students:
            average_marks = sum(student.marks) / len(student.marks)
            print(f"{student.name}: Average Marks = {average_marks:.2f}")

    def __display_students_with_low_attendance(self):
        if not self.students:
            print("No students to display.")
            return
        for student in self.students.values():
            if student.attendance < 75:
                print(f"{student.name}: Attendance = {student.attendance}%")

    def __get_result_status(self):
        if not self.students:
            print("No students to get result status.")
            return
        name = input("Enter student name to get result status: ")
        student = self.students.get(name)
        if not student:
            print("Student not found.")
            return
        average_marks = sum(student.marks) / len(student.marks)
        if average_marks >= 90:
            status = "Excellent"
        elif 75 <= average_marks < 90:
            status = "Very Good"
        elif 50 <= average_marks < 75:
            status = "Pass"
        else:
            status = "Fail"
        print(f"{student.name}: Average Marks = {average_marks:.2f}, Result Status = {status}")


    def __clear_Screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    Student().run()