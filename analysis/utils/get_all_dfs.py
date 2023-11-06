import pandas as pd
import os


def get_all_dfs(path: str, by_year=False) -> list[pd.DataFrame]:
    """Read in all dataframes from csv files in path folder

    Args:
        path (str): The path to the folder containing the csv files
        by_year (bool, optional): Whether or not to combine all courses from the same year into one dataframe.
        If this is enabled, then the function will return a dictionary of dataframes with keys as year labels.
        Otherwise, the function will return a dictionary of dataframes with keys as semester labels. 
        Defaults to False.

    Returns:
        list[pd.DataFrame]: List of dataframes
    """
    # Read in all dataframes from csv files in path folder
    # Return dictionary of dataframes with keys as semester labels
    semesters = {}
    wd = os.getcwd()
    # Change path to include working directory
    path = os.path.join(wd, path)
    for filename in os.listdir(path):
        f = os.path.join(wd, path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            sem_name = f"{filename[0:4]}_{filename[4:6]}"
            semesters[sem_name] = pd.read_csv(f)

    if by_year:
        # Combine all semesters from the same year into one dataframe
        # Return dictionary of dataframes with keys as year labels
        years = {}
        for sem in semesters:
            year = sem[0:4]
            if year in years:
                years[year] = pd.concat([years[year], semesters[sem]])
            else:
                years[year] = semesters[sem]
        return years

    return semesters
