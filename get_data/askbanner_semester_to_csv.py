# Save all courses for a given semester to a CSV file
# Uses askBanner to get the courses, allowing for parsing of any semester

from parse_single_course import parse_course
import csv
from bs4 import BeautifulSoup
import requests

# This is the delimiter used in the CSV file. It is a comma by default, but '\t' could be used for a .tsv
DELIMETER = ','


def get_courses(semesterID: str) -> list[dict]:
    """Take a semesterID and return a list of courses for that semester in dictionary format
    See course_details.py and parse_course.py for more info on the dictionary format

    Args:
        semesterID (str): the semesterID in the form of YYYYSS (e.g. 202103 for Spring 2021)

    Returns:
        list[dict]: a list of courses for the given semesterID
    """
    # Get the page. If form data (semester) is sent as anything else (e.g. JSON) it may not work.
    data = f"session={semesterID}&dept=&instr=&type=&day=&time=&unit=&format=&division_search=&crse_level_search=&submit=Submit"
    page = requests.post(
        "https://aisapps.vassar.edu/cgi-bin/courses.cgi", data=data)

    # Get all divs
    soup = BeautifulSoup(page.content, 'html.parser')
    div_courses = soup.find_all("div")

    processed_courses = []
    for div_course in div_courses:
        raw_course = div_course.text
        try:
            course = parse_course(raw_course)
        except Exception as e:
            print(f"Error parsing course: {e}")
            print(f"Raw course: {raw_course}")
            print(f"skipping this course...")
            continue

        processed_courses.append(course)

    return processed_courses


def save_courses_for_sem(semesterID: str, path) -> None:
    """Save the courses for a given semester to a CSV file at the given path

    Args:
        semesterID (_type_): _description_
        path (_type_): _description_
    """
    all_courses = get_courses(semesterID)
    print(f"Found & downloading {len(all_courses)} listings for {semesterID}")
    # Write to CSV
    keys = all_courses[0].keys()
    with open(path, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, delimiter=DELIMETER)
        dict_writer.writeheader()
        dict_writer.writerows(all_courses)
