from mycollege.controllers import student
from .utils import banner


def add(stud_id, name, age, subjects):
    is_added = student.admit(stud_id, name, age, subjects)
    if is_added:
        print(f"Student with {stud_id} admitted successfully.")
    else:
        print(f"Error while admitting student with id={stud_id}")


def display_all():
    students = student.get_all()
    for stud in students:
        banner(stud)
