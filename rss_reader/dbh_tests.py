import unittest
from database_handler import *
from unittest.mock import patch, Mock


class MyTest(unittest.TestCase):
    @patch("database_handler.DataBaseHandler")
    def test_create_table(self, mock_DataBase):
        m = mock_DataBase
        m.create_table()
        m.create_table.assert_called()

    @patch("database_handler.DataBaseHandler")
    def test_emptiness_checker(self, mock_DataBase):
        m = mock_DataBase
        m.emptiness_checker()
        m.emptiness_checker.assert_called()




if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)