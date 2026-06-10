"""Helper functions for column manipulation and cleaning.
"""

import re
import string
from typing import Any, Iterable, Union

import numpy as np
import pandas as pd

# Patterns for normalizing merge keys
REGEX_NAME_PATTERN = f'[{re.escape(string.punctuation) + string.whitespace}]'
REGEX_TEAM_PATTERN = r'.*\b(\w+)$'

# Historical team names for mapping to current team names
WASHINGTON_TEAM_NAMES = ['Washington Redskins', 'Washington Football Team']
HOUSTON_TEAM_NAMES = ['Houston Oilers', 'Tennessee Oilers']

# Position categories
DEFENSIVE_BACKS = ['FS', 'SS', 'CB']
DEFENSIVE_LINEMAN = ['DE', 'DT']
OFFENSIVE_LINEMAN = ['OC', 'OG', 'OT']
RUNNING_BACKS = ['FB']


def column_to_lowercase(series: pd.Series) -> pd.Series:
    """Return a lowercased copy of a Series.

    Args:
        series (pd.Series): pandas Series of strings.

    Returns:
        pd.Series: Lowercased series.
    """
    return series.str.lower()


def column_strip_whitespace(series: pd.Series) -> pd.Series:
    """Strip leading and trailing whitespace from a Series.

    Args:
        series (pd.Series): pandas Series of strings.

    Returns:
        pd.Series: Stripped series.
    """
    return series.str.strip()


def column_remove_pattern(
        series: pd.Series, pattern: str, replace_with: str
) -> pd.Series:
    """Remove a regex pattern from a Series.

    Args:
        series (pd.Series): pandas Series of strings.
        pattern (str): Regular expression pattern to replace.
        replace_with (str): String to replace the pattern with.

    Returns:
        pd.Series: Series with the pattern replaced.
    """
    return series.str.replace(pattern, replace_with, regex=True)


def column_replace_value(
    series: pd.Series, values_to_replace: Iterable[Any], replace_with: Any
) -> pd.Series:
    """Replace values in a Series, returning a Series.

    Args:
        series (pd.Series): pandas Series of strings.
        values_to_replace (Iterable[Any]): Values to replace.
        replace_with (Any): Value to replace with.

    Returns:
        pd.Series: Series with values replaced.
    """
    return np.where(series.isin(values_to_replace), replace_with, series)


def column_convert_value(
        series: pd.Series, dtype: Union[type, str]
) -> pd.Series:
    """Convert a Series to a given dtype.

    Args:
        series (pd.Series): pandas Series of strings.
        dtype (Union[type, str]): Data type to convert to.

    Returns:
        pd.Series: Series with converted data type.
    """
    return series.astype(dtype)
