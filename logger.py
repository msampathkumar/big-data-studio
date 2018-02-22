import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

# logging.error('hello!')
# logging.debug('This is a debug message')
# logging.info('this is an info message')
# logging.warning('tbllalfhldfhd, warning.')

def new_print(prefix, some_input):
    print(prefix, some_input)

# ipython notebooks are not so smart here.
logger.info = lambda x: new_print('INFO:', x)
logger.debug = lambda x: new_print('DEBUG:', x)
logger.warning = lambda x: new_print('WARNING:', x)
logger.warning = lambda x: new_print('WARNING:', x)
logger.error = lambda x: new_print('ERROR:', x)
