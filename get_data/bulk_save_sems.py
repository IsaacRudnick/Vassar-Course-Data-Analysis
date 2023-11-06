import os
import requests
from bs4 import BeautifulSoup
import ab_sem_to_csv as dl_courses  # For downloading courses


def get_valid_semester_ids() -> list[str]:
    """Check the AskBanner website to get all available semester options

    Returns:
        list[str]: a list of semesterIDs
    """

    html = requests.get("https://aisapps.vassar.edu/cgi-bin/geninfo.cgi").text
    soup = BeautifulSoup(html, 'html.parser')
    # Get all option elements in the <select name="session"> element
    options = soup.find('select', {'name': 'session'}).find_all('option')
    # Get the value attribute of each option element
    semesters = [o['value'] for o in options]

    return semesters


def bulk_save_semesters(semesterIDs: list[str], directory: str) -> None:
    """Save all the courses for the given semesters to CSV files in the given directory

    Args:
        semesterIDs (list[str]): the list of semesters to save
        directory (str): the local directory to save the CSV files
    """
    if not os.path.exists(directory):
        os.mkdir(directory)

    for semesterID in semesterIDs:
        dl_courses.save_courses_for_sem(semester, os.path.join(directory, f'{semesterID}.csv'))


if __name__ == "__main__":
    # The location of the directory to save the CSV files
    directory = "./analysis/courses"
    # Get all the valid semesters currently available in AskBanner
    semesters = get_valid_semester_ids()

    bulk_save_semesters(semesters, directory)
