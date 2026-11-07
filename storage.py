
from rich.console import Console
import json
import os
from course import c
from university import myuni
from student import s
from professor import p

console = Console()
FILE_NAME = "university_data.json"


# Validate JSON data
def validate_data(data):

    if not isinstance(data, dict):
        raise TypeError("University data must be a dictionary.")

    required_keys = [
        "students",
        "professors",
        "courses",
        "student_marks",
        "student_grades",
        "student_courses",
        "professor_courses"
    ]
    if len(data["students"]) != len(data["student_grades"]):
        raise ValueError("Student and grade records are inconsistent.")

    if len(data["students"]) != len(data["student_courses"]):
        raise ValueError("Student and course records are inconsistent.")

    if len(data["professors"]) != len(data["professor_courses"]):
        raise ValueError("Professor and course records are inconsistent.")

    for key in required_keys:
        if key not in data:
            raise KeyError(f"Missing required key: {key}")

    for key in required_keys:
        if not isinstance(data[key], list):
            raise TypeError(f"Invalid data type for {key}. Expected a list.")


# Save university data
def save_data(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        

    except (OSError, TypeError, ValueError) as e:
        console.print(f"[bold red]Error saving university data: {e}[/bold red]")


# Load JSON data
def load_data():

    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        validate_data(data)
        return data

    except json.JSONDecodeError:
        console.print("[bold red]Error: Invalid JSON file.[/bold red]")
        return None

    except (TypeError, KeyError) as e:
        console.print(f"[bold red]Error: Invalid university data: {e}[/bold red]")
        return None

    except OSError as e:
        console.print(f"[bold red]File error: {e}[/bold red]")
        return None


# Restore university data
def load_university_data(s, p, c, myuni):

    data = load_data()

    if data is None:
        return

    if not data:
        console.print("[bold red]No saved university data found.[/bold red]")
        return

    # Restore main records
    s._student[:] = data["students"]
    p._professor[:] = data["professors"]
    c.courses[:] = data["courses"]

    # Restore student grades
    s._student_grades[:] = data["student_grades"]
    s._student_marks[:]  = data["student_marks"]

    # Initialize relationship lists
    s.student_courses[:] = [[] for _ in s._student]
    p._course_assigned[:] = [[] for _ in p._professor]
    c.student_enroll[:] = [[] for _ in c.courses]
    c.course_assigned[:] = [[] for _ in c.courses]

    # Rebuild student-course relationships
    saved_student_courses = data["student_courses"]

    for i, course_records in enumerate(saved_student_courses):

        if i >= len(s._student):
            break

        for saved_course in course_records:

            for j, course in enumerate(c.courses):

                if course[1] == saved_course[1]:

                    s.student_courses[i].append(course)

                    if s._student[i] not in c.student_enroll[j]:
                        c.student_enroll[j].append(s._student[i])

                    break

    # Rebuild professor-course relationships
    saved_professor_courses = data["professor_courses"]

    for i, course_records in enumerate(saved_professor_courses):

        if i >= len(p._professor):
            break

        for saved_course in course_records:

            for j, course in enumerate(c.courses):

                if course[1] == saved_course[1]:

                    p._course_assigned[i].append(course)

                    if p._professor[i] not in c.course_assigned[j]:
                        c.course_assigned[j].append(p._professor[i])

                    break

    # Restore university records
    myuni._students[:] = s._student
    myuni._professors[:] = p._professor
    myuni._courses[:] = c.courses
