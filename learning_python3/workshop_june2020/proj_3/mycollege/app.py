from mycollege.views import student

def main():
    print("Welcome to My College!")
    student.display_all()
    student.add(2, 'Faizan', 25, ['Python'])
    student.add(3, 'Imran', 25, ['Python'])
    print("After adding -")
    student.display_all()

if __name__ == '__main__':
    main()