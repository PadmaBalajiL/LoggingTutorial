import TestClass as test
import logging

# Creating logger
logger = logging.getLogger('example')
logger.setLevel(logging.DEBUG)
# logging.basicConfig(filename ='example.log')

# creating console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# file handler
fh =logging.FileHandler('example.log')
fh.setLevel(logging.ERROR)

# create formatter
formatter = logging.Formatter('%(asctime)s  -%(name)s  -%(levelname)s  -%(message)s')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)
# application code
logger.debug('Debug message')
test_obj = test.Test1()


'''
import logging.config

logging.config.fileConfig('logging.conf')
# ls = test.Test1()

# Create logger
logger = logging.getLogger('example')

# Application code
logger.debug('Debug Message')

logger = logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%d-%m %H:%M',
    filename='application.log',
    filemode='w')
'''
