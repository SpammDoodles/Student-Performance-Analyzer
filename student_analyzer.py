import matplotlib.pyplot as plt
import csv

#------------------------------------- Task 1 ------------------------
students = []

#------------------------------------- Task 2 -------------------------


def calculate_final_score(mid,final,assignment):
    return (0.4 * mid) + (0.5 * final) + (0.1 * assignment) 

def assign_letter_grade(score):
    if score >= 85 and score <= 100:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 55:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"
    
    return grade

def add_student():
    global students

    id = int(input("Enter the student id: "))
    name = input("Enter the name of student: ")
    midterm = int(input("Enter the Midterm marks: "))
    final = int(input("Enter the Final Exam marks: "))
    assignment = int(input("Enter the assignment marks: "))

    final_score = int(calculate_final_score(midterm,final,assignment))
    grade = assign_letter_grade(final_score)

    student = {"id": id,
               "name": name,
               "midterm": midterm,
               "final": final,
               "assignment": assignment,
               "final_score": final_score,
               "grade": grade
            }
    students.append(student)  
    print("student added successfully.")  

def remove_student():
    global students
    if not students:
        print("No student is available in the students data")
        return
    id = int(input("Enter the id of the student you want to remove:"))
    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("student removed successfully")
            return
    print("student not found")

def update_student():
    global students

    if not students:
        print("There is no record to update")
        return
    id = int(input("Enter the sid to update data:"))
    for s in students:
        if s["id"] == id:
            s["midterm"] = int(input("Enter new midterm marks: "))
            s["final"] = int(input("Enter new final marks: "))
            s["assignment"] = int(input("Enter new assignment marks: "))
            s["final_score"] = int(calculate_final_score(s["midterm"],s["final"],s["assignment"]))
            s["grade"] = assign_letter_grade(s["final_score"])

            print("record successfully updated")
            return
    print("Student id not found")

def search_student():
    global students
    print()
    id = int(input("Enter the student id: "))
    for s in students:
        if s["id"] == id:
            print()
            print(f"{'ID':<5}{'Name':<15}{'Mid':<10}{'Final':<10}{'Assign':<12}{'Score':<12}{'Grade':<8}")
            print(f"{s["id"]:<5}{s["name"]:<15}{s["midterm"]:<10}{s["final"]:<10}{s["assignment"]:<13}{s["final_score"]:<12}{s["grade"]:<8}")
            return
    print("student not found")

def show_all_students():
    global students
    if not students:
        print("No student in the database")
        return
    
    sorted_students = sorted(students,key = lambda s: s["id"])
    print(f"{'ID':<5}{'Name':<15}{'Mid':<10}{'Final':<10}{'Assign':<12}{'Score':<12}{'Grade':<8}")
    for s in sorted_students:
        print(f"{s["id"]:<5}{s["name"]:<15}{s["midterm"]:<10}{s["final"]:<10}{s["assignment"]:<13}{s["final_score"]:<12}{s["grade"]:<8}")
        


#------------------------------------- Task 3 ------------------------------

def save_students():
    global students
    if not students:
        return
    with open("students.csv","w",newline = "") as f:
        fields = ["id","name","midterm","final","assignment","final_score","grade"]
        writer = csv.DictWriter(f,fieldnames = fields)
        writer.writeheader()

        for d in students:
            writer.writerow(d)
    print("saving {} students to the file".format(len(students)))


def load_students():
    try:
        with open("students.csv","r",newline = "") as f:
            reader = csv.DictReader(f)
            for s in reader:
                s["id"] = int(s["id"])
                s["midterm"] = int(s["midterm"])
                s["final"] = int(s["final"])
                s["assignment"] = int(s["assignment"])
                s["final_score"] = int(s["final_score"])
                students.append(s)   
    except FileNotFoundError:
        print("NO file found starting with empty student list")
    
#------------------------------------- Task 4 ------------------------------

class Student:
    def __init__(self, id, name, mid, final, assignment):
        self.id = id
        self.name = name
        self.mid = mid
        self.final = final
        self.assignment = assignment
        self.final_score = self.compute_final()
        self.grade = self.compute_grade(self.final_score)
    
    def compute_final(self):
        return (0.4 * self.mid) + (0.5 * self.final) + (0.1 * self.assignment) 
        
    def compute_grade(self,score):
        if score >= 85 and score <= 100:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 55:
            grade = "C"
        elif score >= 40:
            grade = "D"
        else:
            grade = "F"
        
        return grade
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "mid": self.mid,
            "final": self.final,
            "assignment": self.assignment,
            "final_score": self.final_score,
            "grade": self.grade
        }

#-------------------------------------  Task 5 ------------------------------

def generate_report():
    global students
    if not students:
        print("No students available.")
        return
    
    sorted_students = sorted(students, key = lambda s: s["final_score"], reverse = True)
    grades = {}
    for s in students:
        grades[s["grade"]] = grades.get(s["grade"],0) + 1
    
    print()
    print(" STUDENT REPORT ".center(70,"="))

    print("\nStudents Sorted by Final Score (Descending):")
    print(f"{'ID':<5}{'Name':<15}{'Score':<12}{'Grade':<8}")

    for s in sorted_students:
        print(f"{s["id"]:<5}{s["name"]:<15}{s["final_score"]:<12}{s["grade"]:<8}")
    
    scores = [s["final_score"] for s in students]
    
    print("\nTotal Students:", len(students))
    print("Highest Final Score:", max(scores))
    print("Lowest Final Score:", min(scores))
    print("Average Final Score:", round(sum(scores) / len(students),2))

    print("\nGrade Distribution: ")
    for grade,count in grades.items():
        print("{}: {}".format(grade,count))

#-------------------------------------  Task 5 ------------------------------


def visualize_grades():
    if not students:
        print("No students to visualize.")
        return

    grades = {}
    for s in students:
        g = s["grade"] 
        grades[g] = grades.get(g, 0) + 1

    grade_labels = sorted(grades.keys())
    grade_counts = [grades[s] for s in grade_labels]

    plt.bar(grade_labels, grade_counts,label = "Students", color='purple', edgecolor = "black")
    plt.legend()
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Grade Distribution")
    plt.yticks(range(max(grade_counts) + 3))
    plt.show()

#------------------------------------- main ------------------------------


def main():
    load_students()
    while True:
        print()
        print("Student Analyzer".center(100,"="))
        print("\n1- Add student")
        print("2- Remove student")
        print("3- Search student")
        print("4- Update student")
        print("5- Show all students")
        print("6- Generate Report")
        print("7- Visualize grades")
        print("8- Exit")
        print()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            remove_student()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            show_all_students()
        elif choice == 6:
            generate_report()
        elif choice == 7:
            visualize_grades()
        elif choice == 8:
            save_students()
            print("Exiting..")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

