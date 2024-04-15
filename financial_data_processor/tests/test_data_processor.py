import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor

class TestDataProcessor(TestCase):
    """The following constant has been provided to reduce the amount of 
    code needed when creating DataProcessor class objects in the tests that 
    follow.  To use the constant, prefix it with self.  Examples:
    self.INPUT_DATA
    e.g.:  data_procesor = DataProcessor(self.INPUT_DATA)
    """
    INPUT_DATA = [{"Transaction ID":"1" ,"Account number":"1001" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1000,"Currency":"CAD","Description":"Salary"}, 
                {"Transaction ID":"2" ,"Account number":"1002" ,
                "Date":"2023-03-01" ,"Transaction type": "deposit",
                "Amount":1500,"Currency":"CAD","Description":"Salary"}]






if __name__ == "__main__":
    unittest.main()
