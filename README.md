# Course Data Scraper and Analysis Tool

This tool scrapes the data from the Vassar College schedule and allows for analysis of the data.

## Project files and structure:

- `ab_courses_to_csv.py` - Allows for scraping of the Vassar College schedule and saving the data to a CSV file.
  Call `save_courses_for_sem(semester, path)` using the semester (YYYYSS) (where SS is 01: Spring 02: Summer, or 03: Fall) and path to save the data to a CSV file.
- `deprecated/sb_courses_to_csv.py` - Allows for easy scraping of currently loaded semester courses, but not other semesters. Easier to parse data, but parsing is handled by:
- `parse_course.py` which handles the processing of the `raw_course` text block provided by webscraping
- `course_details.py` which is essentially documentation for what a course is and what it contains (description of fields, explanation of data availability)

## How it works:

(assuming use of bulk_save_sems to save all available semesters, as opposed to using an individual util for smaller-scale scraping)

- The scraper uses the [requests](https://pypi.org/project/requests/) library to get the HTML of the schedule page, and then uses [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to parse the HTML.
- The scraper then uses `re` to find the `raw_course` text block, which contains all the course data in a single string.
- The scraper then uses `parse_course.py` to parse the `raw_course` string into a list of `Course` objects.
- The scraper then uses `csv` to save the list of `Course` objects to a CSV file.

## I want to run my own analysis on the data:

- First, download the data to your local machine. See `get_data/README.md` for instructions.
- The data will be available as a JSON Object or a CSV file, depending on your choice. It is recommended to use [pandas](https://pandas.pydata.org/) for analysis, as it is a powerful tool for data analysis and the utility functions in `get_data/utils/` may be specific to [pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) (a form of table).
