"""Helper functions for reading and writing csv files
"""

import pandas as pd
import string
import re
import numpy as np

def csv_write(df, file_path):
    df.to_csv(file_path, index=False)

def csv_read(file_path, delimiter):
    return pd.read_csv(file_path, delimiter=delimiter)
