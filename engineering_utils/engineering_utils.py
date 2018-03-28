import pandas as pd
from inspect import isfunction

def check_str(user_input):
    if type(user_input) != str:
        raise TypeError("Expected input is str, received: " + str(user_input))
def check_str_list(user_input):
    if not type(user_input) in [str, list]:
        raise TypeError("Expected input is str/list, received: " + str(user_input))
    if type(user_input) == str:
        [check_str(_) for _ in user_input]
def check_fns(user_input):
    if not isfunction(user_input):
        raise TypeError("Expected input is function, received: " + str(user_input))

def check_config_vectors(engineering_config):
    if not set(list(map(len, engineering_config))) == set([3]):
        raise Exception("Expector config is a list of set of size 3")



def config_checker(engineering_config, default_columns=[]):
    '''
    To check provided config is structure.
    '''
    check_config_vectors(engineering_config)
    
    newly_added_columns = []
    def check_col_req(req_col):
        all_known_cols = list(default_columns + newly_added_columns)
        if type(req_col) == str:
            return req_col in all_known_cols
        if type(req_col) == list:
            unknown_cols = [_ for _ in req_col if _ not in all_known_cols]
            if unknown_cols:
                return False
            else:
                return True
    for new_col, req_col, new_col_func in engineering_config:
        check_str(new_col)
        check_str_list(req_col)
        check_fns(new_col_func)
        if check_col_req(req_col):
            newly_added_columns.append(new_col)
        else:
            raise KeyError('Missing/Mis-spelled Column: ' + str(req_col))


def config_mapper(engineering_config):
    '''
    To Apply engineering config to data columns
    '''
    for new_column, required_col, function in data_engineering_config:
        if type(required_col) == str:
            # ONLY ONE COLUMN
            new_df[new_column] = new_df[required_col].apply(function)
        if type(required_col) == list:
            # Multi-column - axis=1
            new_df[new_column] = new_df[required_col].apply(function, axis=1)
