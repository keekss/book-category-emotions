import os

# Change project directory if needed.
PROJECT_DIR = os.getcwd()
DATA_DIR    = f'{PROJECT_DIR}/data'
STATS_DIR   = f'{PROJECT_DIR}/stats'

PATHS = dict(
    'books_raw' = f'{DATA_DIR}/books_raw.csv'
)


path = lambda name: PATHS[name]
    