import pandas as pd
import os


def get_all_dfs(path):
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

    return semesters
