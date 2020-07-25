import csv

from ..settings import STORAGE_FILE
from ..exceptions import IntegrityError

def _save(student_obj):
    with open(STORAGE_FILE, mode="a", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=student_obj.keys())
        writer.writerow(student_obj)

def _fetch():
    with open(STORAGE_FILE, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(map(lambda rec: dict(
            id=rec['id'],
            name=rec['name'].capitalize(),
            age=int(rec['age']),
            subjects=rec['subjects'].split('|'),
            is_junior=True if int(rec['age'])<18 else False
            ), reader))

def add_student(stud_id, name, age, subjects):
    student_obj = {
        'id': stud_id,
        'name': name.lower(),
        'age': age,
        'subjects': '|'.join(subjects)
    }

    if get_student(stud_id):
        raise IntegrityError(f"The student object with id = {stud_id} already exists.")

    _save(student_obj)
    return True

def get_student(stud_id):
    for stud in _fetch():
        if stud_id == stud['id']:
            return stud

def get_students():
    return _fetch()