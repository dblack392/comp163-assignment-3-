#Code going into first commit.
student_name = "De'Aundre Black"
current_gpa = 3.0
study_hours = 5
social_points = 40
stress_level = 80
#Second commit code.
mode_choice = input()
easy_mode = ("Easy Difficulty: (12 Credits)")
medium_mode = ("Medium Difficulty: (15 Credits)")
hard_mode = ("Hard Difficulty: (18 Credits)")
#social_points was evaluated on a scale of 0-50
#stress_level was evaluated on a scale of 0-100
print(f"Student Name: {student_name}")
print(f"Current Gpa: {current_gpa:.2f}")
print(f"Study hours: {study_hours}")
print(f"Social Point: {social_points}")
print(f"Stress level: {stress_level}")

print("")
print("Enter your choice:")
if mode_choice == easy_mode:
    print(f"Mode: {easy_mode}")
elif mode_choice == medium_mode:
    print(f"Mode: {medium_mode}")
elif mode_choice == hard_mode:
    print(f"Mode: {hard_mode}")
else:
    print("Invalid Choice: Choose Mode again")