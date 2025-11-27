import json
import os

class StudentManagement:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_student(self, name, roll, marks):
        student = {
            "name": name,
            "roll": roll,
            "marks": marks,
            "average": sum(marks.values()) / len(marks)
        }
        self.data.append(student)
        self.save_data()

    def remove_student(self, roll):
        self.data = [s for s in self.data if s["roll"] != roll]
        self.save_data()

    def get_student(self, roll):
        for s in self.data:
            if s["roll"] == roll:
                return s
        return None

    def display_all(self):
        for s in self.data:
            print(s)

def main():
    sms = StudentManagement()

    while True:
        print("\n1 Add Student")
        print("2 Remove Student")
        print("3 Get Student")
        print("4 Display All")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            marks = {}
            for subject in ["Math", "Science", "English"]:
                marks[subject] = int(input(f"Enter marks for {subject}: "))
            sms.add_student(name, roll, marks)

        elif choice == "2":
            roll = input("Enter roll to remove: ")
            sms.remove_student(roll)

        elif choice == "3":
            roll = input("Enter roll: ")
            print(sms.get_student(roll))

        elif choice == "4":
            sms.display_all()

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
