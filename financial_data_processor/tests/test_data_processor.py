import unittest
from data_processor.data_processor import DataProcessor
class TestDataProcessor(unittest.TestCase):
    INPUT_DATA = [{ "Transaction ID": "1","Account number": "1001",
            "Date": "2023-03-01","Transaction type": "deposit",
            "Amount": 1000,"Currency": "CAD","Description": "Salary"},
        {"Transaction ID": "2","Account number": "1002",
            "Date": "2023-03-01","Transaction type": "withdrawal",
            "Amount": 1500,"Currency": "CAD","Description": "Salary"}]
    def test_update_account_summary_deposit(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        # Act
        data_processor.update_account_summary(self.INPUT_DATA[0])  
        # Assert
        account_summary = data_processor.account_summaries["1001"]
        self.assertEqual(account_summary["balance"], 1000)
        self.assertEqual(account_summary["total_deposits"], 1000)
    def test_update_account_summary_withdrawal(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        # Act
        data_processor.update_account_summary(self.INPUT_DATA[1])  
        # Assert
        account_summary = data_processor.account_summaries["1002"]
        self.assertEqual(account_summary["balance"], -1500)
        self.assertEqual(account_summary["total_withdrawals"], 1500)
    def test_check_suspicious_transactions_large_amount(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        # Act
        data_processor.check_suspicious_transactions(self.INPUT_DATA[0])
        # Assert
        self.assertFalse(data_processor.suspicious_transactions)  
    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        input_data = [self.INPUT_DATA[1]]  
        data_processor = DataProcessor(input_data)
        # Act
        data_processor.process_data()  
        # Assert
        self.assertFalse(data_processor.suspicious_transactions)  
    def test_update_transaction_statistics(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        # Act
        data_processor.update_transaction_statistics(self.INPUT_DATA[0])
        # Assert
        stats = data_processor.transaction_statistics["deposit"]
        self.assertEqual(stats["total_amount"], 1000)
        self.assertEqual(stats["transaction_count"], 1)
    def test_get_average_transaction_amount(self):
        # Arrange
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor.process_data()  
        # Act
        deposit_average = data_processor.get_average_transaction_amount("deposit")
        withdrawal_average = data_processor.get_average_transaction_amount("withdrawal")
        # Assert
        self.assertEqual(deposit_average, 1000.0)
        self.assertEqual(withdrawal_average, 1500.0)  
if __name__ == "__main__":
    unittest.main()