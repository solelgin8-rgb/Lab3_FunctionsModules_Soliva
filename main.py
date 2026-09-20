# main.py
import grades

# Student Identity Configuration
LAST_NAME = "Soliva"         # Replace with your surname
STUDENT_ID = "TUPM-26-4154"  # Replace with your ID 

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate Student-Unique Scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)

print("=" * 40)
print(f"Student Profile: {LAST_NAME} ({STUDENT_ID})")
print(f"Generated Dataset Scores: {scores}")
print(f"Calculated Academic Average: {round(average, 2)}%")
print(f"Final Assigned Evaluation Grade: {grade}")
print(f"Performance Review Metric: {remark}")
print("=" * 40)