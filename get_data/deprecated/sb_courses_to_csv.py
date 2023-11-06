# Save all courses for a given semester to a CSV file
# Uses scheduleBrewer to get currently offered courses
# This is simpler to parse but only works for the current semester

import csv
import asyncio
import aiohttp

# API URL
url = 'https://schedulebrewer.vassar.edu/api/search/'


async def fetch_courses(session, url, i):
    params = {'page': str(i)}
    async with session.get(url, params=params) as response:
        response_json = await response.json()
        return response_json.get('results', [])

all_courses = []
# Max # of pages to get
max_pages = 200

tasks = []
async with aiohttp.ClientSession() as session:
    for i in range(1, max_pages + 1):
        task = asyncio.create_task(fetch_courses(session, url, i))
        tasks.append(task)

    courses_lists = await asyncio.gather(*tasks)
    for courses in courses_lists:
        all_courses.extend(courses)

print(f"{len(all_courses)} courses found")
print(all_courses[100])

for course in all_courses:
    if course['courselength'] != 1:
        print(course['courselength'], course)

# Write to CSV
keys = all_courses[0].keys()
with open('courses.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_courses)
