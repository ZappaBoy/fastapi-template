from utils.logger import Logger


class Core:

    def __init__(self):
        self.logger = Logger('Core')

    def test(self):
        return 'Tested'
