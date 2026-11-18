"""
Problem-2: Student management system in Python
Write a program to build a simple Student Management System using Python which can perform the following operations:

Accept - This method takes details from the user like name, roll number, and marks for two different subjects.

Display - This method displays the details of every student.

Search - This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number

Delete - This method deletes the record of a particular student with a matching roll number.

Update - This method updates the roll number of the student. This method will ask for the old roll number and new roll number. It will replace the old roll number with a new roll number.

Operations used,

1.Accept Student details
2.Display Student Details
3.Search Details of a Student
4.Delete Details of Student
5.Update Student Details
6.Exit

List of Students

Name : A
RollNo : 1
Marks1 : 100
Marks2 : 100

Name : B
RollNo : 2
Marks1 : 90
Marks2 : 90

Name : C
RollNo : 3
Marks1 : 80
Marks2 : 80

Search method output:

Student Found,
Name : B
RollNo : 2
Marks1 : 90
Marks2 : 90

 

Click to add a cell.
"""

class Student:

    def __