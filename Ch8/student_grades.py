
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
    elif command == '2':
        # ...
        del student_grades[input("Enter name: ")]
    elif command == '3':
        # ...
        print(student_grades[input("Enter name: ")])
    elif command == '4':
        break
    else:
        print('Unrecognized command.')
