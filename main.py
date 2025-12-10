"""
This file is the starting file for Innomatics LMS projects
And it contains business logic of LMS

authors : ragasudha@gmail.com
copy rights : 2025@Innomatics.
"""

import sys
sys.path.append(r"C:\Users\Ragasudha\OneDrive\Desktop\Innomatics\LMS>")

from assets.data import initialize_data
from commons.login import login
from utils.admin_utils import process_request
from utils.display_utils import (
    display_admin_options,
    display_login_options,
    display_student_options,
    display_teacher_options
)

def main():
    """
    Main function is a starting point for LMS.
    """
    print("="*50)
    print("Welcome to LMS")
    print("="*50)
    # Initializing our data
    login_status, turn_off, selected = display_login_options()
    if turn_off:
        print("Turning Off the software")
        return # successfull Return
    # login_status = login()
    if login_status:
        initialize_data()
        if selected == "ADMIN":
            choice = display_admin_options()
            process_request(choice)
        elif selected == "STUDENT":
            display_student_options()
        elif selected == "TEACHER":
            display_teacher_options()
        status = True
        while status:
            login_status, turn_off, selected = display_login_options()
            if turn_off:
                print("Turning Off the Software")
                status = False
    else:
        print("Unsuccessful Login.Exiting LMS.Please try again.")

if __name__ == "__main__":
    # you can write Statements 
    main() 
