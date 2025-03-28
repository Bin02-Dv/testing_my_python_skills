students = ["Alice", "Bob", "Charlie", "David", "Eva"]
scores = {"Alice": 95, "Bob": 90, "Charlie": 88, "David": 85, "Eva": 80}

sorted_students_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# print("Here are the top 3")

# for i, (name, score) in enumerate(sorted_students_scores[:3], start=1):
#     print(f"{i}. {name} scored ({score})")

# print("Students Grade")

# for name, score in sorted_students_scores:
#     grade = ''
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     else:
#         grade = "D"
#     print(f"{name} scored {score}, and his Grade is {grade}")

# total_number_of_students = len(scores.keys())
# highest_score = max(scores.values())
# lowest_score = min(scores.values())
# total_scores = sum(scores.values())
# average_score = total_scores / total_number_of_students

# for name, score in sorted_students_scores:
#     student = ''
#     if score == highest_score:
#         student = name
#         print(f"Highest score is: {student} with {highest_score}")
#     elif score == lowest_score:
#         student = name
#         print(f"Lowest score is: {student} with {lowest_score}")
#         print(f"Average score is: {average_score}")

total_number_of_students = len(scores)
highest_scorer = max(scores, key=scores.get)
lowest_scorer = min(scores, key=scores.get)
total_scores = sum(scores.values())
average_score = round(total_scores / total_number_of_students, 2)

print("Student Performance Summary:")
print(f"- Highest Score: {highest_scorer} with {scores[highest_scorer]}")
print(f"- Lowest Score: {lowest_scorer} with {scores[lowest_scorer]}")
print(f"- Average Score: {average_score}")
        
    