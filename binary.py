import pickle

import pickle

def write_data_to_file():
    """Write student data to a binary file."""
    with open('marks.dat', 'wb') as file:
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            student = {'roll_no': roll_no, 'name': name, 'marks': marks}
            pickle.dump(student, file)
    print("Data written to marks.dat successfully!")

def display_high_scorers():
    """Display students with marks greater than 95."""
    try:
        with open('marks.dat', 'rb') as file:
            print("Students scoring more than 95 marks:")
            while True:
                try:
                    student = pickle.load(file)
                    if student['marks'] > 95:
                        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("The file marks.dat does not exist. Please write data to the file first.")

# Main Program
while True:
    print("\nMenu:")
    print("1. Write data to file")
    print("2. Display high scorers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        write_data_to_file()
    elif choice == 2:
        display_high_scorers()
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
