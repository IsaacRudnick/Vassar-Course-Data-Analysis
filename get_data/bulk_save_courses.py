import os
import ab_courses_to_csv as dl_courses  # For downloading courses

start_year = 1996
end_year = 2024
ignore = ["202403"]  # Semesters to ignore

directory = "analysis/courses"
if not os.path.exists(directory):
    os.mkdir(directory)

years = range(start_year, end_year+1)
# This ignores the summer sessions (2)
sessions = [1, 3]
for y in years:
    for s in sessions:
        semester = f"{y}0{s}"
        if semester in ignore:
            continue
        # print(f"Getting courses for {semester}")
        dl_courses.save_courses_for_sem(semester, os.path.join(directory, f'{semester}.csv'))
