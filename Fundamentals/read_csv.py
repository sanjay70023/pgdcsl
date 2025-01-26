# Write a Python script to read a CSV file containing student records and 
# perform operations like sorting by name or calculating the average marks.

import csv

# Function to read a CSV file and return its content
def read_csv(file_path):
    students = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            students.append(row)
    return students

# Function to sort students by name
def sort_by_name(students):
    return sorted(students, key=lambda x: x['Name'])

# Function to calculate the average marks
def calculate_average(students):
    total_marks = sum(float(student['Marks']) for student in students)
    return total_marks / len(students)

# Example usage
file_path = 'students.csv'
students = read_csv(file_path)

sorted_students = sort_by_name(students)
print("Sorted Students by Name:")
for student in sorted_students:
    print(student)

average_marks = calculate_average(students)
print(f"\nAverage Marks: {average_marks}")