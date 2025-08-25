from pprint import pprint

# Student Management System.
# Add student.
# Remove student.
# Update student record.
# Get a student.
# Display all students.



# We first create a empty dictionary that will carry all student 
# And the student record inside the first dictionary

students_db = {}
student_id = 0
def add_function():
	print('I am executing add student logic.')
	name = input('Enter student name:\n>>')
	age = int(input('Student Age:\n>>'))
	department = input('Department:\n>>')
	key = len(students_db) + 1
	students_db[key] = {'name': name, 'age': age, 'department': department}
	pprint(students_db)

def delete_student():
	student_id = int(input('Student ID to delete:\n>>'))
	if student_id in students_db:
		del students_db[student_id]
		print(f'Student with ID {student_id} deleted successfully')
		pprint(students_db)

def update_student():
	print('''
	1. Update Name.
	2. Update Age.
	3. Update department.
	''')
	option = int(input('Enter option:\n>>'))
	if option == 1:
		student_id = int(input('Enter ID to update name:\n>>'))
		if student_id in students_db:
			new_name = input('Enter new name:\n>>')
			students_db[student_id]['name'] = new_name
			pprint(students_db)
		else:
			print('ID not found')
	elif option == 2:
		student_id = int(input('Enter ID to update Age:\n>>'))
		if student_id in students_db:
			new_age = input('Enter new name:\n>>')
			students_db[student_id]['age'] = new_age
			pprint(students_db)
		else:
			print('ID not found')
	elif option == 3:
		student_id = int(input('Enter ID to update Department:\n>>'))
		if student_id in students_db:
			new_dept = input('Enter new name:\n>>')
			students_db[student_id]['department'] = new_dept
			pprint(students_db)

def get_student():
	student_id = int(input('Enter student ID to get:\n>>'))
	if student_id in students_db:
		print(f"Name: {students_db[student_id]['name']}, Age: {students_db[student_id]['age']}, Department: {students_db[student_id]['department']}")
	else:
		print('ID NOT FOUND!')


def display_student():
	for student in students_db:
		print(f"Name: {students_db[student]['name']}, Age: {students_db[student]['age']}, Department: {students_db[student]['department']}")

def start_program():
	while True:
		print('''
		1. Add a student.
		2. Delete a student.
		3. Udate a student record.
		4. Get a student.
		5. Display all student.
		>>>''')
		option = int(input('What do you what to do:\nEnter option:\n>>'))
		if option == 1:
			add_function()
			print('I am back to the start function')
		elif option == 2:
			delete_student()
			print('I am back to the start function')
		elif option == 3:
			update_student()
			print('I am back to the start function')
		elif option == 4:
			get_student()
			print('I am back to the start function')
		elif option == 5:
			display_student()
			print('I am back to the start function')
start_program()
		

