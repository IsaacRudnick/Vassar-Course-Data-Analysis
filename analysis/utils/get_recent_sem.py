import pandas as pd
import os


def get_recent_sem(path):
    # Read in all dataframes from csv files in path folder
    # Return dictionary of dataframes with keys as semester labels
    semesters = {}
    wd = os.getcwd()
    # Change path to include working directory
    path = os.path.join(wd, path)
    # Keep track of largest # sem (e.g. 199601 < 202401, so we can use # as a proxy for recency)
    largest_sem = -1
    for filename in os.listdir(path):
        f = os.path.join(wd, path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            largest_sem = max(largest_sem, int(filename[0:6]))

    return pd.read_csv(os.path.join(wd, path, str(largest_sem) + ".csv"))
