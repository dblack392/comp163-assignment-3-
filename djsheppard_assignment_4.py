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
#list of study options for part 3
study_options = ["Programming", "Math", "English", "History"]
#This portion handles the how the mode is chosen, which is by the users choice.
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
#Part 3 for the study choice(some Ai help provided, will show where.)
study_choice = input("Choose a study option (Programming / Math / English / History): ")

if study_choice not in study_options:
    print("Invalid study option. Please select from the list:", study_options)
else:
    #Runs for a valid choice
    print(f"You chose to study: {study_choice}")
    #I didn't understand how to calculate this fully, I had ChatGPT give me a process of how to find this. part
    if (study_choice in ["Programming", "Math"]) and (current_gpa < 3.5):
        study_hours += 2
        current_gpa += 0.10  #Small improvement.
        social_points -= 5   #Less social time.
        print("Focused STEM study: +2 study hours, +0.10 GPA, -5 social points.")

    #I had ChatGPT help me do the if not calculations as I didn't understand it.
    elif (study_choice == "English") or (study_choice == "History"):
        if not (stress_level <= 20):
            stress_level -= 5
            social_points = min(50, social_points + 2)
            print("Humanities study: -5 stress, +2 social points (if not already calm).")
        else:
            print("You're already pretty relaxed, humanities keep you steady.")