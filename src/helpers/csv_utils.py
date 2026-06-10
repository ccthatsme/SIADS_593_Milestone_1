"""Helper functions for reading and writing csv files
"""

from typing import Optional

import pandas as pd


def csv_write(df: pd.DataFrame, file_path: str) -> None:
    """Write a DataFrame to CSV.

    Args:
        df (pd.DataFrame): DataFrame to write.
        file_path (str): Target file path to write the CSV to.
    """
    df.to_csv(file_path, index=False)


def csv_read(file_path: str, delimiter: Optional[str] = ",") -> pd.DataFrame:
    """Read a CSV file into a DataFrame.

    Args:
        file_path (str): Path to the CSV file.
        delimiter (Optional[str], optional): Field delimiter

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path, delimiter=delimiter)
