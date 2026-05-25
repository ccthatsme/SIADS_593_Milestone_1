"""Helper functions for column manipulation and cleaning.
"""

import pandas as pd
import string
import re
import numpy as np

# Patterns for normalizing merge keys
REGEX_NAME_PATTERN = f'[{re.escape(string.punctuation) + string.whitespace}]'
REGEX_TEAM_PATTERN = r'.*\b(\w+)$'

# Historical team names for mapping to current team names
WASHINGTON_TEAM_NAMES = ['Washington Redskins', 'Washington Football Team']
HOUSTON_TEAM_NAMES = ['Houston Oilers', 'Tennessee Oilers'] 


# def column_to_lowercase(df, col_name):
#     """Return the specified column lowercased."""
#     return df[col_name].str.lower()

def column_to_lowercase(series):
    """Return a lowercased copy of a Series."""
    return series.str.lower()

def column_strip_whitespace(series):
    """Strip leading and trailing whitespace from a Series."""
    return series.str.strip()

def column_remove_pattern(series, pattern, replace_with):
    """Remove a regex pattern from a Series."""
    return series.str.replace(pattern, replace_with, regex=True)

def column_replace_value(series, values_to_replace, replace_with):
    """Replace values in a Series."""    
    return np.where(series.isin(values_to_replace), replace_with, series)

def column_convert_value(series, type):
    """Convert column type"""    
    return series.astype(type)

# df_draft['name_for_merge'] = df_draft['name'].str.lower().str.strip().str.replace(regex_pattern, "", regex=True)
# df_draft['team'] = np.where(df_draft['team'].isin(washington_team_names), 'commanders', df_draft['team'])
