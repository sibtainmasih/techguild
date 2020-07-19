file_path = './data/story.txt'
with open(file_path, 'a', encoding='utf-8') as f:
    f.writelines("This is line 1\n")
    f.writelines("This is line 2\n")
    f.writelines("This is line 3\n")

with open(file_path, 'r', encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())

import csv

registration_file = './data/registration.csv'

with open(registration_file, 'a+', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([1, 'Alice', 25, '|'.join(['Maths', 'Science'])])
    writer.writerow([2, 'Bob', 26, '|'.join(['Python', 'Data Science'])])
    f.seek(0)
#with open(registration_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for rec in reader:
        print(rec)