# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []

n = int(input("Enter number of applicants: "))
for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    name = input("Student name: ")

    marks = []
    for j in range(5):
        mark = int(input(f"Enter marks in subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / 5
    eligible = (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARKS for mark in marks)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME
    )

    student = {
        "name": name,
        "marks": marks,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "eligible": eligible
    }

    students.append(student)
print("\n----- ELIGIBILITY RESULTS -----")

for student in students:
    if student["eligible"]:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print(
        f'{student["name"]}: '
        f'{student["aggregate"]:.2f}% - {status}'
    )
eligible_students = [
    student for student in students
    if student["eligible"]
]

eligible_students.sort(
    key=lambda student: (
        -student["aggregate"],
        -student["attendance"],
        student["income"],
        student["name"].casefold()
    )
)
print("\n----- SCHOLARSHIP RANKING -----")

if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"Rank {rank}: {student['name']} | "
            f"Aggregate: {student['aggregate']:.2f}% | "
            f"Attendance: {student['attendance']:.2f}% | "
            f"Income: Rs.{student['income']:.2f}"
        )
else:
    print("No eligible students found.")

print("\nScholarship allocation process completed.")
