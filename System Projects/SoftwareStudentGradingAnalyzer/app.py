print("Student Grade Analyzer")
# Function to calculate average grade
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)
# Function to determine letter grade
def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
# Main function to analyze student grades
def analyze_student_grades():
    student_name = input("Enter the student's name: ")
    grade = []
    while True:
            g = input("Enter a grade (or 'done' to finish): ")
            if g.lower() == 'done':
                break
            grade.append(float(g))


           # writing the grade to a file  
    with open("grades.txt", "a") as file:
                lines = f"{student_name}: {grade}\n"
                file.write(lines)
    print("Saved grades to file!\n")

# Reading file

    with open("grades.txt", "r") as file:
        print("Grades from file:")
        for line in file:
            print(line.strip())

# Run the grade analyzer
if __name__ == "__main__":
    analyze_student_grades()
