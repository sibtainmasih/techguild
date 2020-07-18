from mycollege.models.student import add_student, get_students


def admit(stud_id, name, age, subjects):
    if age<8:
        return False
    
    return add_student(stud_id, name, age, subjects)

def get_all():
    # Authorization
    return get_students()