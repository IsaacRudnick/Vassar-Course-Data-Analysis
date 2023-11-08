# Course Data Scraper and Analysis Tool

This tool scrapes the data from the Vassar College schedule and allows for analysis of the data. \
Because GitHub will show the output of these cells, this works as a library of pre-run analysis without requiring the user to run the code themselves.

## How it works:

(assuming use of bulk_save_sems to save all available semesters, as opposed to using an individual util for smaller-scale scraping)

- The scraper uses the [requests](https://pypi.org/project/requests/) library to get the HTML of the schedule page, and then uses [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to parse the HTML.
- The scraper then uses `re` to find the `raw_course` text block, which contains all the course data in a single string.
- The scraper then uses `parse_course.py` to parse the `raw_course` string into a list of `Course` objects.
- The scraper then uses `csv` to save the list of `Course` objects to a CSV file.

## I want to run my own analysis on the data:

- First, download the data to your local machine. See `get_data/README.md` for instructions.
- The data will be available as a JSON Object or a CSV file, depending on your choice of scraping sub-module. It is recommended to use [pandas](https://pandas.pydata.org/) for analysis, as it is a powerful tool for data analysis and the utility functions in `analysis/utils/` may be specific to [pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) (a form of table).

## Project files and structure:

### `get_data/`

Handles scraping of the Vassar College schedule and saving the data to a JSON Object or CSV file. This is an overview of the provided files:

- `ab_courses_to_csv.py` - Allows for scraping of the Vassar College schedule and saving the data to a CSV file.
  Call `save_courses_for_sem(semester, path)` using the semester (YYYYSS) (where SS is 01: Spring 02: Summer, or 03: Fall) and path to save the data to a CSV file. Parses with:

- `parse_course.py` which handles the processing of the `raw_course` text block provided by webscraping

- `course_details.py` which is essentially documentation for what a course is and what it contains (description of fields, explanation of data availability)

> - `deprecated/sb_courses_to_csv.py` - Allows for easy scraping of currently loaded semester courses, but not other semesters. Easier to parse data, but not as useful.

### `analysis/`

Handles analysis of the data. All files here have markdown cells (top of file) with explanations of what they do and how they work.

#### `utils/`

- `attribute_percent_per_group.py` - abstracts the process of getting the percentage of courses with a given attribute per group (e.g. percentage of courses per department that are year-long)
- `get_all_dfs.py` - abstracts the process of getting all the dataframes (presumably in the `analysis/courses/` folder)
  allows for easy merging of semesters in same year to get dataframes with courses by year instead of by semester
- `get_recent_sem.py` - abstracts the process of getting the most recent semester's data (presumably in the `analysis/courses/` folder)

#### `courses/`

This is in the gitignore. However, it is where the dataframes will be saved by the data-scraping module. The dataframes are saved as CSV files.
