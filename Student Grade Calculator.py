# Function to calculate grade and message
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Outstanding!!!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good effort, but you can do even better!"
    elif marks >= 60:
        return "D", "Improvement needed. Don't give up!"
    else:
        return "F", "Give 100% effort next time. You can improve!"

# Input student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Please enter between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

# Get grade and message
grade, message = calculate_grade(marks)

# Display result
print("\nRESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
