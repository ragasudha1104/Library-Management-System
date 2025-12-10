from assets.data import LMS
from utils.display_utils import (
    display_branch_details,
    display_year_details,
    display_sem_details,
)

def ensure_teacher_path(branch: str, year: str, sem: str):
    """Create missing nested keys so we can safely append."""
    if "TEACHERS" not in LMS:
        LMS["TEACHERS"] = {}

    # ensure branch exists
    if branch not in LMS["TEACHERS"]:
        LMS["TEACHERS"][branch] = {}

    # ensure year exists
    if year not in LMS["TEACHERS"][branch]:
        LMS["TEACHERS"][branch][year] = {}

    # ensure sem exists and is a list
    if sem not in LMS["TEACHERS"][branch][year]:
        LMS["TEACHERS"][branch][year][sem] = []


def add_teacher():
    while True:
        print("\nADD NEW TEACHER")
        branch = str(display_branch_details())
        year = str(display_year_details())
        sem = str(display_sem_details())
        subject = input("Enter subject name: ").strip()
        name = input("Enter teacher name: ").strip()
        password = input("Enter teacher password: ").strip()

        teacher =  {"name": name, "password": password, "subject": subject}
        
        # Create any missing nested objects before appending
        ensure_teacher_path(branch, year, sem)

        LMS["TEACHERS"][branch][year][sem].append(teacher)

        #print(f"{name} ({subject}) successfully added to {branch}, Year {year}, Sem {sem}.")
        print(f"Successfully registered teacher: {name} | Subject: {subject} | Department: {branch} | Year: {year} | Semester: {sem}")

        more = input("Do you want to add another teacher (Y/N)? ").strip().upper()
        if more != "Y":
            break


