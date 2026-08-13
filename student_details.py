def analyze_result(name, roll, marks):
    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)

    # Assign grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Display student details
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")

    # Find subjects below 40
    below_40 = []

    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"Subject {i + 1}")

    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("Subjects below 40: None")


# Student details
name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

# Call the function
analyze_result(name, roll, marks)