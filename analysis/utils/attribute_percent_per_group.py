import matplotlib.pyplot as plt
from utils.get_recent_sem import *
from types import FunctionType as function

courses = get_recent_sem("courses")


def attribute_per_group(course_has_attribute: function, group_from_course: function, attribute_descr: str, group_descr: str):
    """Generates a bar chart showing the percentage of courses in each group that have a given attribute.
    The attribute is determined by the course_has_attribute function, which takes a course as input and returns a boolean.
    The group is determined by the group_from_course function, which takes a course as input and returns a string.

    Args:
        course_has_attribute (function): A function that takes a course as input and returns a boolean.
        group_from_course (function): A function that takes a course as input and returns a string.

        attribute_descr (str): A description of the attribute being analyzed for labelling bar chart.
        group_descr (str): A description of the group being analyzed for labelling bar chart.
    """
    # Format: {group: [attribute_count, total_count], ...}
    group_course_info = {}

    for index, course in courses.iterrows():
        group = group_from_course(course)

        # Add dept to dict if it doesn't exist
        if group not in group_course_info:
            group_course_info[group] = [0, 0]

        # Increment total_count regardless of course details
        group_course_info[group][1] += 1

        # If course has attribute, increment attribute_count
        if course_has_attribute(course):
            group_course_info[group][0] += 1

    group_attribute_percent = {
        group: group_course_info[group][0] / group_course_info[group][1] for group in group_course_info}

    # Make bar chart wider
    plt.figure(figsize=(12, 5))
    # Add titles (must be done after setting figure size)
    plt.title(f"Percentage of Courses {attribute_descr} by {group_descr}")
    plt.xlabel("Department")
    plt.ylabel("Percentage")
    # Rotate x-axis labels
    plt.xticks(rotation=90)

    # Set y-axis ticks
    yticks = [0.25, 0.5, 0.75, 1]
    plt.yticks(ticks=yticks)
    for y in yticks:
        plt.axhline(y=y, color="gray", linestyle=":")

    # Sort departments by percentage of courses requiring special permission
    data = dict(sorted(group_attribute_percent.items(), key=lambda x: x[1]))
    plt.bar(data.keys(), data.values())

    average = sum(data.values()) / len(data.values())
    plt.axhline(y=average, color="red", linestyle="-",
                label="Average % {attribute_descr}")
    leg = plt.legend(loc='upper left')

    # Show percentage on top of each bar
    for key, value in data.items():
        # but only if the percentage is not 0
        if value > 0:
            # Add spacing to make text more readable
            plt.text(key, value, f"  {round(value*100, 1)}%",
                     ha="center", rotation=90, fontsize=10)

    # Add horizontal space for text labels that are high (e.g. 100%)
    plt.margins(y=0.2)
