from unittest import TestCase

__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2013, Searce'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Vivek.Gour@searce.com'
__status__ = 'Development'


class TestResult(TestCase):
    def test_result(self):
        # if 1 == 2:
        #     self.fail()
        if 1== 1:
            self.fail()
