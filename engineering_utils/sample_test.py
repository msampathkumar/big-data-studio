from engineering_utils import config_mapper, config_checker
import pandas as pd

from nose.tools import assert_raises
from nose.tools import *


sample_data = {
'col1': [100, 200],
'col2': [0.0003, 0.0004],
'col3': ['x-12313', 'y-12313'],
}

sample_df = pd.DataFrame(sample_data)


def test_user_working_input():
    # expected 3 value in config
    sample_engineering_config = [('new_col1', 'col1', lambda x: x)]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())


@raises(Exception)
def test_user_input_error01_list_of_set_three():
    # expected 3 value in config
    sample_engineering_config = [('new_col', 'col1')]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())


@raises(TypeError)
def test_user_input_error02():
    # expected 3 value in config
    sample_engineering_config = [(123123, 'col1', lambda x: x)]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())



@raises(TypeError)
def test_user_input_error03():
    # expected 3 value in config
    sample_engineering_config = [('new_col', 12313, lambda x: x)]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())


def test_user_input_error04():
    # expected 3 value in config
    sample_engineering_config = [('new_col', ['col1'], lambda x: x)]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())


    
def test_dynamic_update_new_cols_to_test_cols():
    sample_engineering_config = [
        ('new_col1', 'col1', lambda x: x/100),
        ('new_col2', 'new_col1', lambda x: x * 1), # col8 does nt exist
    ]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())

def test_example():
    sample_engineering_config = [
        ('new_col1', 'col1', lambda x: x/100),
        ('new_col2', 'col2', lambda x: x * 100),
    ]
    config_checker(sample_engineering_config, default_columns=sample_df.columns.tolist())