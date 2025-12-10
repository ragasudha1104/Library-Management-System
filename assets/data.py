from config import *

LMS = {} #global scope
LMS["ADMINS"] = [{"name:SUDHA","password:sudha123"}]

def initialize_data():
    # LMS = {} #LOCAL SCOPE
    LMS["STUDENTS"] = {}
    LMS["TEACHERS"] = {}
    LMS["BOOKS"] = {}

    for dept in DEPTS:
        LMS["STUDENTS"][dept] = {}
        for year in YEARS:
            LMS["STUDENTS"][dept][year] = {}
            for sem in SEMS:
                LMS["STUDENTS"][dept][year][sem] = {}