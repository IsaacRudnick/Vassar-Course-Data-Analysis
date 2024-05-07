import re

fields_positions = {
    'courseID': 0,
    'title': 13,
    'units': 44,
    'sp': 50,
    'max': 53,
    'enr': 57,
    'avl': 61,
    'wl': 65,
    'gm': 69,
    'yl': 74,
    'pr': 77,
    'fr': 80,
    'la': 83,
    'qa': 86,
    'format': 89,
    'xlist': 96,
    'd1': 112,
    'time1': 118,
    'd2': 134,
    'time2': 118,
    'loc': 134,
    'instructor': 145}


def parse_course(raw_course: str) -> dict:
    """Parses raw course text block into a dictionary of course details

    Args:
        raw_course (str): the contents of a course element from the AskBanner website

    Returns: a dictionary of course details (overview below, more details in course_details.py)

    """

    course = {}

    fields = list(fields_positions.keys())
    positions = list(fields_positions.values())

    for i in range(len(positions)):
        # Get the start and end positions for the field (e.g., 0-13 for courseID)
        start_position = positions[i]
        end_position = positions[i+1] if i+1 < len(positions) else None

        field_name = fields[i]
        field_value = raw_course[start_position:end_position].strip()

        course[field_name] = field_value

    course['courselength'] = courselength_from_rc(raw_course)
    course['dept'] = course['courseID'].split('-')[0]

    return course


def courselength_from_rc(raw_course):
    # See course_details lookups["courselength"]
    if "1st 6 Weeks" in raw_course:
        return 2
    elif "2nd 6 Weeks" in raw_course:
        return 3
    else:
        return 1
