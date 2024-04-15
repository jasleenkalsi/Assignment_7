import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler

class InputHandlerTests(TestCase):
    """The following constant has been provided to reduce the amount of 
    code needed when testing the InputHandler class in the tests that 
    follow.  To use the constant, prefix it with self.  Examples:
    self.FILE_CONTENTS
    e.g.:  with patch("builtins.open", mock_open(read_data = self.FILE_CONTENTS)):
    """
    FILE_CONTENTS = ("Transaction ID,Account number,Date,Transaction type,"
                + "Amount,Currency,Description\n"
                + "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
                + "2,1002,2023-03-01,deposit,1500,CAD,Salary\n"
                + "3,1001,2023-03-02,withdrawal,200,CAD,Groceries") 









if __name__ == "__main__":
    unittest.main()