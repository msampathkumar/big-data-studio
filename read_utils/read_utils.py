"""

TODO
* Convert all sub functions into dunder form
* add documentation with examples
"""

import pandas as pd
import os
import os.path as path
import logging

__all__ = ['read_data', 'merge_data', 'concat_data']

logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog.log', mode='a')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fhandler.setFormatter(formatter)
# logger.addHandler(fhandler)
# logger.setLevel(logging.DEBUG)

# logging.error('hello!')
# logging.debug('This is a debug message')
# logging.info('this is an info message')
# logging.warning('tbllalfhldfhd, warning.')

logger.info = lambda x: new_print('INFO:', x)
logger.debug = lambda x: new_print('DEBUG:', x)
logger.warning = lambda x: new_print('WARNING:', x)
logger.warning = lambda x: new_print('WARNING:', x)
logger.error = lambda x: new_print('ERROR:', x)


read_functions = {
    '.csv' : pd.read_csv,
    '.html': pd.read_html,
    '.json': pd.read_json,
    '.pkl': pd.read_pickle,
    '.pickle': pd.read_pickle,
}

HTML_TABLE = 0

def read_data(user_input):
    if os.path.isfile(user_input):
        main_df = read_file(user_input)
    elif os.path.isdir(user_input):
        main_df = read_dir(user_input)
    return main_df

def merge_data():
    return pd.merge

def concat_data():
    return pd.concat

def new_print(prefix, some_input):
    print(prefix, some_input)

def find_pointer(filename):
    for file_extension, file_reader in read_functions.items():
        if filename.endswith(file_extension):
            logging.info('Reading file(' + file_extension + ')\t using function -' + str(file_reader.__name__))
            return file_reader

def read_file(file):
    """
    Returns DF from a file(csv/json/..)
    """
    logger.info('read file - csv/json/...')
    file_reader_fns = find_pointer(file)
    dataframe = file_reader_fns(file)
    if file_reader_fns.__name__ == pd.read_html.__name__:
        # read_html returns a list of dataframes in html page
        dataframe = dataframe[HTML_TABLE]
    logger.info('--' * 15)
    return dataframe


def read_dir(user_input):
    """
    Read a directory
    """
    logger.info('==' * 15)
    dir_path, dir_subdirs, all_files = list(os.walk(user_input))[0]
    all_dfs = []
    for file in all_files:
        file = os.path.join(dir_path, file)
        logger.info('Reading - ' + file)
        try:
#             print(locals())
            df = read_file(file)
#             print(df.head(5))
#             logger.info(file + str( df.shape))
            all_dfs.append(df)
        except:
            raise logging.exception('Failed to load file')
    if all(map(lambda x: x.__class__  == pd.core.frame.DataFrame, all_dfs)):
        return pd.concat(all_dfs)
    else:
        logger.debug('Received a non dataframe object while reading files!')
        logger.debug('Printing files list')
        logger.debug(str(all_files))
        logger.debug('Print types of dataframes received')
        logger.debug(str(list(
            map(lambda x: x.__class__ , all_dfs)
        )))
        return all_dfs


# result = read_dir(sample_folder)

