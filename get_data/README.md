# Getting Data

## What data is available?

The data is available as defined in `course_details.py`

## I want the data for the latest semester

Check the `deprecated/sb_courses_to_csv.py` file. This file is deprecated because it only allows for scraping of the currently loaded semester, but it is easier to parse the data. This technique is entirely valid assuming the semester at [Vassar's ScheduleBrewer](https://schedulebrewer.vassar.edu/) is the one you want (look at the top of the page to see the semester). It will save everything to `courses.csv` in the current working directory.

## I want the data for a specific semester

Check the `ab_courses_to_csv.py` file. This file allows for scraping of any semester, but the data parsing (done in `parse_course.py`) may be confusing. This is because the info provided by AskBanner for each course is a block of text that frequently has missing values, edge cases, and more, which requires complicated [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression) to parse robustly and effectively.

## I want the data for all (or many) semesters

See `bulk_save_sems.py` for relevant code. If run directly, this file will save every available semester as a separate csv file.

## Where is the course description?

Because many courses don't provide a description, it is not included in the files. If you want it included anyway, you can uncomment the relevant line in the `parse_course.py` file.