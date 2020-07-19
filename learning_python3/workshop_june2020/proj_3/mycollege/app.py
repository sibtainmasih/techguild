from mycollege.views import student

def main():
    print("Welcome to My College!")
    student.display_all()
    try:
        student.add(2, 'Faizan', 25, ['Python'])
        student.add(3, 'Imran', 7, ['Python'])
    except ValueError as e:
        print(f"{e!r}")
        
    print("After adding -")
    student.display_all()

if __name__ == '__main__':
    main()