
"""
GradeBook Analyzer
Student: Pari Jain
Roll No.: 2501730301
Date: 2025-11-26
Course: Programming for Problem Solving using Python
"""

import csv
import statistics
import os


def calculate_average(marks_dict):
    if not marks_dict:
        return 0.0
    return round(sum(marks_dict.values()) / len(marks_dict), 2)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0.0
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    if not marks_dict:
        return None, None
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

def find_min_score(marks_dict):
    if not marks_dict:
        return None, None
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]


def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def build_gradebook(marks_dict):
    return {name: assign_grade(score) for name, score in marks_dict.items()}

def grade_distribution(grades_dict):
    dist = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades_dict.values():
        if g in dist:
            dist[g] += 1
    return dist


def passed_failed_lists(marks_dict, pass_mark=40):
    passed = [name for name, score in marks_dict.items() if score >= pass_mark]
    failed = [name for name, score in marks_dict.items() if score < pass_mark]
    return passed, failed


def print_results_table(marks_dict, grades_dict):
    header = f"{'Name':<20}{'Marks':>8}{'Grade':>10}"
    print(header)
    print("-"*len(header))
    for name, score in marks_dict.items():
        grade = grades_dict.get(name, "")
        print(f"{name:<20}{score:>8}{grade:>10}")
    print()


def read_csv_to_marks(path):
    marks = {}
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row: 
                    continue
                
                name = row[0].strip()
                try:
                    score = float(row[1].strip())
                except (IndexError, ValueError):
                    print(f"Skipping invalid line: {row}")
                    continue
                marks[name] = score
    except FileNotFoundError:
        print(f"File not found: {path}")
    return marks

def export_grade_table_csv(path, marks_dict, grades_dict):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for name, score in marks_dict.items():
            writer.writerow([name, score, grades_dict.get(name, "")])


def manual_entry():
    print("Enter student data. To stop enter an empty name.")
    marks = {}
    while True:
        name = input("Student name: ").strip()
        if name == "":
            break
        score_str = input("Marks (0-100): ").strip()
        try:
            score = float(score_str)
        except ValueError:
            print("Invalid marks — please enter a number.")
            continue
        marks[name] = score
    return marks


def analyze_marks(marks_dict):
    if not marks_dict:
        print("No data to analyze.")
        return

    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    max_name, max_score = find_max_score(marks_dict)
    min_name, min_score = find_min_score(marks_dict)

    grades = build_gradebook(marks_dict)
    dist = grade_distribution(grades)
    passed, failed = passed_failed_lists(marks_dict)

    print("\n=== Analysis Summary ===")
    print(f"Total students: {len(marks_dict)}")
    print(f"Average: {avg}")
    print(f"Median: {med}")
    print(f"Highest: {max_name} -> {max_score}")
    print(f"Lowest:  {min_name} -> {min_score}")
    print("\nGrade distribution:")
    for grade in ["A","B","C","D","F"]:
        print(f" {grade}: {dist[grade]}")
    print()
    print("Passed students:", len(passed))
    print("Failed students:", len(failed))
    print()

    print_results_table(marks_dict, grades)

    
    ans = input("Do you want to export results to CSV? (y/n): ").strip().lower()
    if ans == 'y':
        outpath = input("Enter output filename (e.g. results.csv): ").strip()
        if outpath == "":
            outpath = "results.csv"
        export_grade_table_csv(outpath, marks_dict, grades)
        print(f"Exported to {outpath}")


def main_menu():
    while True:
        print("\nGradeBook Analyzer - Menu")
        print("1) Manual entry")
        print("2) Load from CSV")
        print("3) Exit")
        choice = input("Choose option (1/2/3): ").strip()
        if choice == '1':
            marks = manual_entry()
            analyze_marks(marks)
        elif choice == '2':
            path = input("Enter path to CSV (name,marks): ").strip()
            marks = read_csv_to_marks(path)
            analyze_marks(marks)
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "_main_":
    print("Welcome to GradeBook Analyzer")
    main_menu()