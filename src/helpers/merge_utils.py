"""Helper functions for dataset merges
"""

from typing import Optional, Sequence

import pandas as pd


DF_DRAFT_MERGE_KEYS = ['name_for_merge', 'team', 'draft_round', 'year']
DF_RAS_MERGE_KEYS = ['name_for_merge', 'Draft Team', 'Round', 'Year']


def merge_datasets(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_merge_keys: Sequence[str],
    right_merge_keys: Sequence[str],
    how: str = "inner",
    validate: Optional[str] = None,
    indicator: bool = False,
) -> pd.DataFrame:
    """Merge two DataFrames using explicit key lists.

    Args:
        left_df (pd.DataFrame): Left DataFrame to merge.
        right_df (pd.DataFrame): Right DataFrame to merge.
        left_merge_keys (Sequence[str]): Column name(s) to join on.
        right_merge_keys (Sequence[str]): Column name(s) to join on.
        how (str, optional): Type of merge to perform.
        validate (Optional[str], optional): Checks if merge of specified type.
        indicator (bool, optional): Adds a column named `_merge`.

    Returns:
        pd.DataFrame: The merged DataFrame.
    """
    return pd.merge(
        left_df,
        right_df,
        left_on=left_merge_keys,
        right_on=right_merge_keys,
        how=how,
        validate=validate,
        indicator=indicator
    )
