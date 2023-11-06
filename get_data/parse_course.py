import re
import course_details


def parse_course(raw_course: str) -> dict:
    """Parses raw course text block into a dictionary of course details

    Args:
        raw_course (str): the contents of a course element from the AskBanner website

    Returns: a dictionary of course details (overview below, more details in course_details.py)

    """
    course = {}
    # SEE course_details.py for more info on each key
    course['courseID'] = courseID_from_rc(raw_course)  # courseID is a unique identifier for each course
    course['dept'] = dept_from_rc(raw_course)  # dept is the department that offers the course
    course['title'] = title_from_rc(raw_course)  # title is the name of the course
    course['units'] = units_from_rc(raw_course)  # units is the number of units the course is worth
    course['sp'] = special_permission_from_rc(raw_course)  # sp is whether the course requires special permission
    course['max_enr'] = max_enrollment_from_rc(raw_course)  # max_enr is the maximum number of students that can enroll in the course
    course['enr'] = enrollment_from_rc(raw_course)  # enr is the number of students enrolled in the course while it ran
    course['avl'] = available_seats_from_rc(raw_course)  # avl is the number of seats available in the course
    course['wl'] = waitlist_from_rc(raw_course)  # wl is the number of students on the waitlist for the course
    course['gm'] = grade_mode_from_rc(raw_course)  # gm is the grade mode of the course (NR, SU, or None)
    course['yl'] = year_long_from_rc(raw_course)  # yl is whether the course is year-long
    course['pr'] = provisional_grades_from_rc(raw_course)  # pr is whether the course uses provisional grades
    course['fr'] = first_year_writing_from_rc(raw_course)  # fr is whether the course is a first-year writing course
    course['la'] = language_course_from_rc(raw_course)  # la is whether the course is a language course
    course['qa'] = quantitative_course_from_rc(raw_course)  # qa is whether the course is a quantitative course (satisfies QA req)
    course['prereq'] = has_prerequisite_from_rc(raw_course)  # prereq is whether the course has a prerequisite
    course['format'] = format_from_rc(raw_course)  # format is the format of the course (CLS, INT, or OTH)
    course['xlist'] = xlist_from_rc(raw_course)  # xlist is the cross-listed course (if any)
    timing = timing_from_rc(raw_course)  # timing is the timing of the course (d1, time1, starttime1, endtime1, duration1, loc1, d2, time2, starttime2, endtime2, duration2, loc2)
    # Add all timing keys and values to course
    for key, value in timing.items():
        course[key] = value

    course['instructor'] = instructor_from_rc(raw_course)
    course['lab_instructor'] = lab_instructor_from_rc(raw_course)
    # course['description'] = description_from_rc(raw_course)
    course['division'] = division_from_rc(raw_course)
    course['courselength'] = courselength_from_rc(raw_course)

    return course


def courseID_from_rc(raw_course):
    pattern = r'[A-Za-z]{3,4}-\d{3}-[0-9A-Za-z]{1,2}\.?'
    match = re.search(pattern, raw_course)
    return match.group()


def dept_from_rc(raw_course):
    return courseID_from_rc(raw_course).split('-')[0]


def title_from_rc(raw_course):
    # The regex pattern '\s+(.*?)\s+\d+\.\d+' is used to find a portion of the input_string that starts
    # with spaces, followed by any text, and ends with a space before a number with a decimal point.

    # We use match.group(1) to access the text captured by the first (and only) set of parentheses in the pattern.
    # This allows us to extract the specific part of the string we're interested in, which is the text between
    # the courseID+spaces and the decimal. Otherwise, the courseID and units # are included in the match.group() call.

    # There are edge cases inclued. For example, some classes are section "G" instead of a standard number. Some class names end with a period, too.
    pattern = r'[A-Za-z]{3,4}-\d{3}-[0-9A-Za-z]{1,2}\.?\s+(.*?)\s+\d+\.\d'
    match = re.search(pattern, raw_course)
    return match.group(1)


def units_from_rc(raw_course):
    pattern = r'\d+\.\d+'
    match = re.search(pattern, raw_course)
    return match.group().strip()


def special_permission_from_rc(raw_course):
    return ' SP ' in raw_course


def _nth_num_in_string(string, n):
    # helper method
    pattern = r'\b\d+\b'
    matches = re.findall(pattern, string)
    return int(matches[n-1])


def max_enrollment_from_rc(raw_course):
    return _nth_num_in_string(raw_course, 1)


def enrollment_from_rc(raw_course):
    return _nth_num_in_string(raw_course, 2)


def available_seats_from_rc(raw_course):
    return _nth_num_in_string(raw_course, 3)


def waitlist_from_rc(raw_course):
    return _nth_num_in_string(raw_course, 4)


def grade_mode_from_rc(raw_course):
    if ' NR ' in raw_course:
        return 'NR'
    elif ' SU ' in raw_course:
        return 'SU'
    else:
        return None


def year_long_from_rc(raw_course):
    return ' YL ' in raw_course


def provisional_grades_from_rc(raw_course):
    return ' PR ' in raw_course


def first_year_writing_from_rc(raw_course):
    return ' FR ' in raw_course


def language_course_from_rc(raw_course):
    return ' LA ' in raw_course


def quantitative_course_from_rc(raw_course):
    return ' QA ' in raw_course


def has_prerequisite_from_rc(raw_course):
    return ' Y ' in raw_course


def format_from_rc(raw_course):
    if ' CLS ' in raw_course:
        return 'CLS'
    elif ' INT ' in raw_course:
        return 'INT'
    elif ' OTH ' in raw_course:
        return 'OTH'


def xlist_from_rc(raw_course):
    pattern = r'X.{4}(?:\/[A-Z]{4})*'
    match = re.search(pattern, raw_course)
    if match:
        return match.group()
    return None


def _location_from_rc(raw_course):
    timing_pattern = r'[MTWRF]{1,3}\s*[\d]{4}(AM|PM)-[\d]{4}(AM|PM)'
    rc_after_timing = re.split(timing_pattern, raw_course)[-1].strip()
    split_timing = rc_after_timing.split(' ')
    # Some courses have no location (e.g. IND) or location is not yet set (locations are set close to start of semester)
    if len(split_timing) < 2:
        return None

    formatted = f"{split_timing[0]} {split_timing[1]}"
    return formatted


def timing_from_rc(raw_course):

    timing = {"d1": None, "time1": None, "starttime1": None, "endtime1": None, "duration1": None, "loc1": None,
              "d2": None, "time2": None, "starttime2": None, "endtime2": None, "duration2": None, "loc2": None}
    pattern = r'([MTWRF]{1,3})\s*([\d]{4}(AM|PM)-[\d]{4}(AM|PM))'
    matches = re.findall(pattern, raw_course)

    # Some courses don't meet at all (e.g. IND courses)
    if len(matches) == 0:
        return timing

    first_slot = matches[0]

    timing['d1'] = first_slot[0]
    time1 = first_slot[1]
    timing['time1'] = time1
    split_time1 = time1.split('-')
    timing['starttime1'] = int(split_time1[0][0:2])*60 + int(split_time1[0][2:4]) + (12*60 if "PM" in split_time1[0] else 0)
    timing['endtime1'] = int(split_time1[1][0:2])*60 + int(split_time1[1][2:4]) + (12*60 if "PM" in split_time1[0] else 0)
    timing['duration1'] = timing['endtime1'] - timing['starttime1']
    timing['loc1'] = _location_from_rc(raw_course)

    # For some courses (e.g. with labs), there will be a second slot
    if len(matches) > 1:
        second_slot = matches[1]

        timing['d2'] = second_slot[0]
        time2 = second_slot[1]
        timing['time2'] = time1
        split_time1 = time1.split('-')
        timing['starttime2'] = int(split_time1[0][0:2])*60 + int(split_time1[0][2:4]) + (12*60 if "PM" in split_time1[0] else 0)
        timing['endtime2'] = int(split_time1[1][0:2])*60 + int(split_time1[1][2:4]) + (12*60 if "PM" in split_time1[0] else 0)
        timing['duration2'] = timing['endtime1'] - timing['starttime1']
        # Remove first time slot from raw_course to ignore what would have been first match
        rc_after_timing = raw_course.split(time1)[-1].strip()
        timing['loc2'] = _location_from_rc(rc_after_timing)

    return timing


def instructor_from_rc(raw_course):
    # Only accept matches after the course type to avoid courses w/ names that look like instructors' names.
    # (e.g. "Language, Empires, Nations" would otherwise match "Languages, Empires" as the name)
    pattern = r'(CLS|INT|OTH).*([A-Z][A-Za-z]*, [A-Z][A-Za-z]*)'
    match = re.search(pattern, raw_course)
    # Some courses have no instructor (e.g. CEL courses) see: https://offices.vassar.edu/community-engaged-learning/
    return match.group(2) if match else None


def lab_instructor_from_rc(raw_course):
    pattern = r'[A-Z][A-Za-z]*, [A-Z][A-Za-z]*'
    match = re.findall(pattern, raw_course)
    return match[1] if len(match) > 1 else None


def description_from_rc(raw_course):
    pattern = r'<p>(.*?)<\/p>'
    match = re.search(pattern, raw_course)
    if match:
        return match.group(1)
    return None


def division_from_rc(raw_course):
    divisions = ['AR', 'FL', 'IP', 'IS', 'NS', 'SS']
    for division in divisions:
        # Add space to capture isolated elements.
        # Example: "AR" may be in course name. " AR " will likely not be
        if (f" {division} ") in raw_course:
            return division


def courselength_from_rc(raw_course):
    # See course_details lookups["courselength"]
    if "1st 6 Weeks" in raw_course:
        return 2
    elif "2nd 6 Weeks" in raw_course:
        return 3
    else:
        return 1
