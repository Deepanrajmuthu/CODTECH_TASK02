class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades)

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average == 100:
            return 10.0
        elif average >= 90:
            return 9.0
        elif average >= 80:
            return 8.0
        elif average >= 70:
            return 7.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0


def main():
    students = {}

    while True:
        print("1. Add student")
        print("2. Add grade")
        print("3. Get average and letter grade")
        print("4. Get GPA")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            students[name] = Student(name)

        elif choice == '2':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            students[name].add_grade(subject, grade)

        elif choice == '3':
            name = input("Enter student name: ")
            average = students[name].get_average()
            letter_grade = students[name].get_letter_grade(average)
            print(f"Average grade for {name}: {average:.2f}")
            print(f"Letter grade for {name}: {letter_grade}")

        elif choice == '4':
            name = input("Enter student name: ")
            average = students[name].get_average()
            gpa = students[name].get_gpa(average)
            print(f"GPA for {name}: {gpa:.2f}")

        elif choice == '5':
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

