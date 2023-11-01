lookups = {}
# Course properties are as follows:

# courseID - Format (DEPT-###-##) where ### is the course number and ## is the section number
# dept - Department (same as DEPT in courseID)
# title - Course title (e.g. 'Introduction to Computer Science')

# units - Number of units (e.g. 1.0 or 0.5)
# sp - Special permission required (either True or False)
# max_enr - Maximum enrollment (e.g. 30)
# enr - Current enrollment (e.g. 30)
# avl - Available seats (e.g. 0)
# wl - Waitlist (e.g. 0)
# gm - Grade Modes (below)
lookups['gm'] = {'NR': 'Non-Recorded Option', 'SU': 'Ungraded'}

# yl - Year Long (either True or False)
# pr - Provisional Grades (either True or False)
# fr - First Year Writing Seminar (either True or False)
# la - Language Course (either True or False)
# qa - Quantitative Course (either True or False)
# prereq - Has a prerequisite (either True or False)

# format - Format of course. Either 'CLS' (for 'Classroom') or 'INT' (for 'Intensive') or 'OTH' (for 'Other')
lookups['format'] = {'CLS': 'Classroom', 'INT': 'Intensive', 'OTH': 'Other'}
# xlist - Department with which this course is cross-listed (e.g. 'XCMPU' or 'XCMPU/MATH' if multiple) note 'X' prefix

# --- Below is all scheduling-related information ---#
lookups['days'] = {'M': 'Monday', 'T': 'Tuesday', 'W': 'Wednesday', 'R': 'Thursday', 'F': 'Friday'}
# loc - Location of the course

# d1 - First (set of) day(s) during which the course is offered. See above
# time1 - Time (string) during which the course is offered (e.g. '12:00PM-1:15PM')
# starttime1 - Start time of the course in mins since midnight (e.g. 750) for 12:30PM (12 * 60 + 30 = 750)
# endtime1 - End time of the course (see above for format)
# duration1 - Duration of the course in minutes (e.g. 75)

# d2 - Second (set of) day(s) during which the course is offered (e.g. 'F' for 'Friday') this is used for courses w/ labs
# time2 - Same as time1 but for d2
# starttime2 - Same as starttime1 but for d2
# endtime2 - Same as endtime1 but for d2
# duration2 - Same as duration1 but for d2
# --- This ends scheduling information ---#

# instructor - Instructor of the course
# description - Long format description of the course. Only available from ScheduleBrewer or Catalog

# --- Below are only applicable / available during registration and pre-registration periods ---#
# limits - # of students from each grade allowed to enroll in the course. Format: (SR/JR/SO/FR) (e.g. '5/5/5/5')
# requests - # of students who have preregistered for the course.
# offered - whether the course is still open
# --- This ends pre-registration information ---#

# division - The division of the course.
lookups['division'] = {'AR': 'Arts', 'FL': 'Foreign Language', 'IP': 'Independent', 'IS': 'Multi/Interdisciplinary', 'NS': 'Natural Science', 'SS': 'Social Science'}
# courselength - See below except keys are ints (1, 2, 3 not '1', '2', and '3')
lookups['courselength'] = {'1': 'Full Semester', '2': 'First Six-Week Course', '3': 'Second Six-Week Course'}
# notes
