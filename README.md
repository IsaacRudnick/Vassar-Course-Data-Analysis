# Course Data Scraper and Analysis Tool

This tool scrapes the data from the Vassar College schedule and allows for analysis of the data.

## Project files and structure:

- `ab_courses_to_csv.py` - Allows for scraping of the Vassar College schedule and saving the data to a CSV file.
  Call `save_courses_for_sem(semester, path)` using the semester (YYYYSS) (where SS is 01: Spring 02: Summer, or 03: Fall) and path to save the data to a CSV file.
- `deprecated/sb_courses_to_csv.py` - Allows for easy scraping of currently loaded semester courses, but not other semesters. Easier to parse data, but parsing is handled by:
- `parse_course.py` which handles the processing of the `raw_course` text block provided by webscraping
- `course_details.py` which is essentially documentation for what a course is and what it contains (description of fields, explanation of data availability)
