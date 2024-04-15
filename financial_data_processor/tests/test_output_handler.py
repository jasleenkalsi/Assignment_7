import unittest
from unittest import TestCase
from output_handler.output_handler import OutputHandler


class TestOutputHandler(TestCase):
    """The following constants have been provided to reduce the amount of 
    code needed when creating OutputHandler class objects in the tests that 
    follow.  To use the constants, prefix them with self.  Examples:
    self.ACCOUNT_SUMMARIES
    self.SUSPICIOUS_TRANSACTIONS
    self.TRANSACTION_STATISTICS
    e.g.:  output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, 
                            self.SUSPICIOUS_TRANSACTIONS, self.TRANSACTION_STATISTICS)
    """

    ACCOUNT_SUMMARIES = { '1001': {'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '2', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}}
    
    SUSPICIOUS_TRANSACTIONS = [{"Transaction ID":"1" ,"Account number":"1001" ,
                            "Date":"2023-03-14" ,"Transaction type": "deposit",
                            "Amount":250,"Currency":"XRP","Description":"crypto investment"}  ]

    TRANSACTION_STATISTICS = {'deposit': {'total_amount': 300, 'transaction_count': 2}, 
                            'withdrawal': {'total_amount': 50, 'transaction_count': 1}}
        







if __name__ == "__main__":
    unittest.main()