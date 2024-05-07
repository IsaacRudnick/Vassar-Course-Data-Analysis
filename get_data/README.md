# Getting Data

The easiest way to get the data for all semesters is to run `download_all_semesters.py`. This script will download all the data for all semesters and save it in the `../analysis/courses/` directory. Each semester will be saved in a separate .csv file, with the semester name as the filename. Note that semesters are '01' for spring or '03' for fall (e.g., the fall semester of 2022 is '202203').

Each row is a course with the following information:

- courseID
- title
- units
- special_permission_required
- max_spots
- enrolled_students
- available_seats
- waitlisted_students
- grade_mode
- yearlong
- provisional_grades
- first_year_writing_seminar
- language_course
- quantitative_course
- has_prerequisite
- format
- division
- department
- cross_list
- days_of_week
- time
- location
- instructor
- crn

However, not all of this information is available for each course. For example, some courses do not have a location or time. Courses with no name are generally lab sections of the course one row above it.
To see more information about the data, click 'Submit' on the [course request site](https://aisapps.vassar.edu/cgi-bin/geninfo.cgi) to see the key (top right).
