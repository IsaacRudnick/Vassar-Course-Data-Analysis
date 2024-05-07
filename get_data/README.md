# Getting Data

## What data is available?

The data is available as defined in `course_details.py`

## I want the data for a specific / the latest semester

Use the `askbanner_semester_to_csv.py` file's `get_courses(semesterID: str) -> list[dict]` function.

## I want the data for all (or many) semesters

Run `download_all_semesters.py`. This file will save every available semester as a separate csv file.

## Where is the course description?

Because many courses don't provide a description, it is not included in the files. If you want it included anyway, you can modify the `parse_course.py` file.
