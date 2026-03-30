from model import predict_priority

# --------------------------
# INPUT VALIDATION
# --------------------------

def get_valid_int(prompt, valid_range=None):
    while True:
        try:
            value = int(input(prompt))
            if valid_range and value not in valid_range:
                print("Invalid input. Try again.")
            else:
                return value
        except:
            print("Enter a valid number.")

# --------------------------
# GET SUBJECTS
# --------------------------

def get_subjects():
    subjects = input("Enter subjects (comma separated): ")
    return [s.strip() for s in subjects.split(",")]

# --------------------------
# GET DETAILS
# --------------------------

def get_subject_details(subjects):
    subject_data = []
    print("\nEnter details for each subject:")

    for sub in subjects:
        print(f"\n{sub}")
        d = get_valid_int("Difficulty (1-3): ", [1,2,3])
        c = get_valid_int("Chapters: ")
        days = get_valid_int("Days left: ")

        subject_data.append((sub, d, c, days))

    return subject_data

# --------------------------
# GENERATE TIMETABLE
# --------------------------

def generate_timetable(sorted_plan, total_days=7):

    timetable = {f"Day {i+1}": [] for i in range(total_days)}

    day = 0
    for subject, priority in sorted_plan:
        for _ in range(int(priority)):
            timetable[f"Day {day+1}"].append(subject)
            day = (day + 1) % total_days

    print("\n----- Weekly Timetable -----\n")

    for d, subjects in timetable.items():
        print(f"{d}: ", end="")
        for s in subjects:
            print(s, end=" ")
        print()
# --------------------------
# GENERATE PLAN
# --------------------------

def generate_plan(subject_data):
    results = []

    for sub, d, c, days in subject_data:
        p = predict_priority(d, c, days)
        results.append((sub, p))

    # sort by priority
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n ===== SMART STUDY PLAN ===== \n")

    for sub, p in results:
        if p >= 5:
            level = " High Priority"
        elif p >= 3:
            level = " Medium"
        else:
            level = " Low"

        print(f"{sub.upper()} → Priority Score: {p} ({level})")

    # SAVE TO FILE
    with open("study_plan.txt", "w") as f:
        f.write("SMART STUDY PLAN\n\n")
        for sub, p in results:
            f.write(f"{sub} - Priority {p}\n")

    print("\n Study plan saved to 'study_plan.txt'")

    # GENERATE TIMETABLE
    generate_timetable(results)

# --------------------------
# MENU
# --------------------------

def menu():
    print("\n===== AI SMART STUDY PLANNER =====")
    print("1. Create Study Plan")
    print("2. Exit")

# --------------------------
# MAIN LOOP
# --------------------------

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            subjects = get_subjects()
            subject_data = get_subject_details(subjects)
            generate_plan(subject_data)

        elif choice == '2':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run program
main()
