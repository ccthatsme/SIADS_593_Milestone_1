"""Helper functions for dataset merges
"""

import pandas as pd
import string
import re
import numpy as np

DF_DRAFT_MERGE_KEYS = ['name_for_merge', 'team', 'draft_round', 'year']
DF_RAS_MERGE_KEYS = ['name_for_merge', 'Draft Team', 'Round', 'Year']


# df_merged_draft_base_left = pd.merge(df_draft, df_ras, left_on=['name_for_merge', 'team', 'draft_round', 'year'], right_on=['name_for_merge', 'Draft Team', 'Round', 'Year'], how='left', validate="m:1")
# df_merged_ras_base_right = pd.merge(df_draft, df_ras, left_on=['name_for_merge', 'team', 'draft_round', 'year'], right_on=['name_for_merge', 'Draft Team', 'Round', 'Year'], how='right', validate="m:1")

def merge_datasets(left_df, right_df, left_merge_keys, right_merge_keys, how, validate = None):
    """Merge two datasets"""    
    return pd.merge(left_df, right_df, left_on=left_merge_keys, right_on=right_merge_keys, how=how, validate=validate)