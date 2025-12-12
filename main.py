import csv

def grade_calculator(marks):
    """This function calculates the grade based on marks"""
    if marks >= 90:
        return "A"
    elif marks  >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "Pass"

class Student:
    """This class is responsible for storing student details"""
    def __init__(self):
        self.id = 0
        self.name = ""
        self.mobile = "+91"+""
        self.address = ""
        self.email = ""
        self.marks = 0
        self.student_information = []

    def student_details(self):
        """This function stores student details"""
        student_data = input("Enter student details(Id,Name,Mobile,Address,Email,Marks): ").split(",")
        self.id = int(student_data[0])
        self.name = student_data[1]
        self.mobile = student_data[2]
        self.address = student_data[3]
        self.email = student_data[4]
        self.marks = student_data[5]
        stud={"Id":self.id,"Name":self.name,"Mobile":self.mobile,"Address":self.address,"Email":self.email,"Marks":self.marks,
              "Grade": grade_calculator(int(self.marks))}
        self.student_information.append(stud)


    def print_student_details(self):
        """This function prints student details"""
        print(self.id, self.name, self.mobile, self.address, self.email, self.marks)
        print(self.student_information)

    def search_student(self,id):
        """This function searches for student details"""
        if id == self.id:
            print("Student details found")
        else:
            print("Student details not found")
    def stored_details(self):
        """This function stores student details"""
        field_names = ["Id", "Name", "Mobile", "Address", "Email", "Marks","Grade"]
        with open("student_info.csv", "w", newline="") as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=field_names)
            csvwriter.writeheader()
            csvwriter.writerows(self.student_information)
            csvfile.close()


    def menu(self):
        """This function displays the menu"""
        while True:
            print("Welcome to Student Result Management System"
                  "\n1.Add Student Details"
                  "\n2.Display Student Details"
                  "\n3.Search Student"
                  "\n4.Store Student Details in CSV")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                        self.student_details()
                case 2:
                        self.print_student_details()
                case 3:
                        self.search_student(id=int(input("Enter student id: ")))
                case 4:
                        self.stored_details()
            user_choice = input("Do you want do it again?(y/n)")
            if user_choice == "y":
                continue
            else:
                break


if __name__ == "__main__":
    student = Student()
    student.menu()