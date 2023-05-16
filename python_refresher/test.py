import unittest

import app


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = app.do_stuff(test_param)
        self.assertEquals(result, 15)

unittest.app()