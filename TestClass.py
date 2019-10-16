import logging

module_logger = logging.getLogger('example.test')
class Test1:
    def __init__(self):
        self.logger = logging.getLogger('example.test.Test1')
        self.logger.debug('ERRRRRORRRRRi')
        self.logger.error("Self Function of Test1 class")
        

class Test2:
    def __init__(self):
        print("Self function of Test2 class")
