# This is a helper file that was used to get the dictionary that is used by parse_single_course.py
# It generates a dictionary that maps the field names to the starting index of the field in the raw course text block
# It also renames the fields to the names used in the course_details.py file

header = "COURSE ID    TITLE                          UNITS SP MAX ENR AVL  WL GMOD YL PR FR LA QA PREREQ FORMAT DIV DEPT XLIST           DAYS  TIME            LOCATION   INSTRUCTOR                       CRN"
#          ---------    -----                          ----- -- --- --- --- --- ---- -- -- -- -- -- ------ ------ --- ---- --------------- ----  ----            --------   ----------                     -----
example = "MATH-221-02  Linear Algebra                 1.0       24  24   0   0 NR               QA        CLS    NS  MATH                 MWF   1030AM-1120AM              Lowrance, Lisa                 31811"

old_to_new_names = {'COURSE ID': 'courseID',
                    'TITLE': 'title',
                    'UNITS': 'units',
                    'SP': 'special_permission_required',
                    'MAX': 'max_spots',
                    'ENR': 'enrolled_students',
                    'AVL': 'available_seats',
                    'WL': 'waitlisted_students',
                    'GMOD': 'grade_mode',
                    'YL': 'yearlong',
                    'PR': 'provisional_grades',
                    'FR': 'first_year_writing_seminar',
                    'LA': 'language_course',
                    'QA': 'quantitative_course',
                    'PREREQ': 'has_prerequisite',
                    'FORMAT': 'format',
                    'DIV': 'division',
                    'DEPT': 'department',
                    'XLIST': 'cross_list',
                    'DAYS': 'days_of_week',
                    'TIME': 'time',
                    'LOCATION': 'location',
                    'INSTRUCTOR': 'instructor',
                    'CRN': 'crn'}

old_names = list(old_to_new_names.keys())

# This will be used to map the new field names to the starting index of the field in the raw course text block
fields_positions = {}

for i in range(len(old_names)):
    old_name = old_names[i]
    new_name = old_to_new_names[old_name]

    starting_index = header.index(old_name)
    fields_positions[new_name] = starting_index

# This is because CRN is right-aligned and if it was the same as the others, it would be 2 to the left
fields_positions['crn'] -= 2
