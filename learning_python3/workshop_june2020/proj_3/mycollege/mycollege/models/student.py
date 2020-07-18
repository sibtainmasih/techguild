
_students = [
    {
        'id': 1,
        'age': 26,
        'name': 'Alice',
        'subjects': ['Maths']
    }
]

def add_student(stud_id, name, age, subjects):
    student_obj = {
        'id': stud_id,
        'age': age,
        'name': name,
        'subjects': subjects
    }

    if get_student(stud_id):
        return False

    _students.append(student_obj)
    return True

def get_student(stud_id):
    for stud in _students:
        if stud_id == stud['id']:
            return stud

def get_students():
    return _students