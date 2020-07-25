import sys
from mycollege.views import student


def get_user_action():
    print("=" * 30)
    print("\nSelect an option: ")
    print("1. View all students")
    print("2. Enter a new record")
    print("0. Quit")
    return int(input("Enter your choice: "))


def display_handler():
    print("*" * 30)
    student.display_all()


def insert_handler():
    print("*" * 30)
    print("\n Enter student details.")
    stud_id = input("ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    subjects = input("Subjects (comma separated): ")
    student.add(stud_id, name, age, subjects.split(","))


def default_handler():
    print("Invalid choice. Please select a correct action.")


def terminate_program():
    print("*" * 30)
    print("Thank you for using the app. Visit again.")
    sys.exit()


HANDLERS = {0: terminate_program, 1: display_handler, 2: insert_handler}


def main():
    print("Welcome to My College!")

    while True:
        HANDLERS.get(get_user_action(), default_handler)()


if __name__ == "__main__":
    main()
