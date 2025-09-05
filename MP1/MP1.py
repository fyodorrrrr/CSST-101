"""
Enchanced Mini Expert System: University Logic Rules
With CSV Logging for Record Keeping
"""

import csv
from datetime import datetime

# ----------------- Logic Functions ----------------- #
def impl(P, Q):
    return (not P) or Q # Implication (P -> Q)

def tf(b: bool) -> str:
    return "T" if b else "F"

# --------------------- Logger --------------------- #
def log_result(student_name, rule_name, result):
    with open("logic_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            student_name, rule_name, result
        ])

# ---------- Rule 1: Attendance ---------- #
def attendance_rule(student_name):
    print("\n--- Attendance Rule Checker ---")
    late = input("Is the student late? (T/F): ").strip().upper() == "T"
    excuse = input("Did you bring an excuse letter (T/F): ").strip().upper() == "T"

    result = impl(late, excuse)
    outcome = "Satisfied" if result else "Violated"
    print(f"P = {tf(late)} (Late), Q = {tf(excuse)} (Excuse Letter)")
    print("Result:", outcome)

    log_result(student_name, "Attendance Rule", outcome)

# ---------- Rule 2: Grading ---------- #
def grading_rule(student_name):
    print("\n--- Grading Rule Checker ---")
    try:
        grade = float(input("Enter Student Grade: "))
    except ValueError:
        print("Invalid Grade Input")
        return
    
    P = grade >= 75
    Q = grade >= 75
    result = impl(P, Q)
    outcome = "Satisfied" if result else "Violated"

    print(f"P = {tf(P)} (grade >= 75), Q = {tf(Q)} (Student Passes)")
    print("Result:", outcome)

    log_result(student_name, "Grading Rule", outcome)

# ---------- Rule 3: Login System ---------- #
def login_rule(student_name):
    print("\n--- Login Rule Checker ---")
    correct_password = "admin123"
    attempt = input("Enter Password: ")

    P = (attempt == correct_password) # Password Correct
    Q = (attempt == correct_password) # Access granted if correct

    result = impl(P, Q)
    outcome = "Satisfied" if result else "Violated"

    print(f"P = {tf(P)} (Password Correct), Q = {tf(Q)} (Access Granted)")
    print("Result:", outcome)

    log_result(student_name, "Login Rule", outcome)

# ---------- Rule 4: Bonus Points ---------- #
def bonus_rule(student_name):
    print("\n--- Bonus Points Eligibility Checker ---")
    regular = input("Does the student have regular attendance? (T/F): ").strip().upper() == "T"
    bonus = regular

    result = impl(regular, bonus)
    outcome = "Satisfied" if result else "Violated"

    print(f"P = {tf(result)} (Regular Attendance), Q = {tf(bonus)} (Bonus Eligible)")
    print("Result:", outcome)

    log_result(student_name, "Bonus Rule", outcome)

# ---------- Rule 5: Scholarship Eligibility ---------- #
def scholarship_rule(student_name):
    print("\n--- Scholarship Eligibility Checker ---")

    try:
        grade = float(input("Enter Student Grade: "))
    except ValueError:
        print("Invalid Grade Input")
        return
    
    attendance = input("Does the student have regular attendance? (T/F): ").strip().upper() == "T"
    good_moral = input("Does the student have good moral standing? (T/F): ").strip().upper() == "T"

    # Conditions
    P = grade >= 85          # High grade requirement
    Q = attendance           # Must have regular attendance
    R = good_moral           # Must have good moral

    # Scholarship = P ∧ Q ∧ R
    result = P and Q and R
    outcome = "Eligible" if result else "Not Eligible"

    print(f"P = {tf(P)} (Grade >= 85)")
    print(f"Q = {tf(Q)} (Regular Attendance)")
    print(f"R = {tf(R)} (Good Moral Standing)")
    print("Result:", outcome)

    log_result(student_name, "Scholarship Rule", outcome)


def main():
    print("=== University Logic Rule System ===")
    student_name = input("Enter Student Name: ".strip())

    while True:
        print("\n==============================")
        print("    Main Menu")
        print("==============================")

        print("1) Attendance Rule Checker")
        print("2) Grading Rule Checker")
        print("3) Login System Rule Checker")
        print("4) Bonus Points Checker")
        print("5) Scholarship Eligibility Checker")
        print("6) Exit")

        choice = input("Choose an Option: ").strip()

        match choice:
            case "1": attendance_rule(student_name)
            case "2": grading_rule(student_name)
            case "3": login_rule(student_name)
            case "4": bonus_rule(student_name)
            case "5": scholarship_rule(student_name)
            case "6":
                print("Exiting... Results saved to logic_results.csv")
                break
            case _: print("Unknown Choice")


if __name__ == "__main__":
    # Create CSV with headers if not exist
    with open("logic_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0: # Only write the header if file is empty
            writer.writerow(["Timestamp", "Student Name", "Rule", "Result"])

main()