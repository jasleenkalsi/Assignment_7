import csv

class OutputHandler:
    """
    A class to handle output operations, including writing account summaries, suspicious transactions,
    and transaction statistics to CSV files.
    """

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict) -> None:
        """
        Initializes the OutputHandler class with account summaries, suspicious transactions,
        and transaction statistics.

        Args:
            account_summaries (dict): A dictionary containing account summaries.
            suspicious_transactions (list): A list of suspicious transactions.
            transaction_statistics (dict): A dictionary containing transaction statistics.
        """
        self.__account_summaries = account_summaries
        self.__suspicious_transactions = suspicious_transactions
        self.__transaction_statistics = transaction_statistics
    
    @property
    def account_summaries(self):
        """
        Get the account summaries.

        Returns:
            dict: A dictionary containing account summaries.
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self):
        """
        Get the suspicious transactions.

        Returns:
            list: A list of suspicious transactions.
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self):
        """
        Get the transaction statistics.

        Returns:
            dict: A dictionary containing transaction statistics.
        """
        return self.__transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        Write account summaries to a CSV file.

        Args:
            file_path (str): The file path where the CSV file will be saved.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for account_number, summary in self.__account_summaries.items():
                writer.writerow([
                    account_number,
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
        Write suspicious transactions to a CSV file.

        Args:
            file_path (str): The file path where the CSV file will be saved.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction ID', 'Account number', 'Date', 'Transaction type', 'Amount', 'Currency', 'Description'])

            for transaction in self.__suspicious_transactions:
                writer.writerow([
                    transaction['Transaction ID'],
                    transaction['Account number'],
                    transaction['Date'],
                    transaction['Transaction type'],
                    transaction['Amount'],
                    transaction['Currency'],
                    transaction['Description']
                ])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        Write transaction statistics to a CSV file.

        Args:
            file_path (str): The file path where the CSV file will be saved.
        """        
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction type', 'Total amount', 'Transaction count'])

            for transaction_type, statistic in self.__transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic['total_amount'],
                    statistic['transaction_count']
                ])
   
    def filter_account_summaries(self, filter_field: str, filter_value: int, filter_mode: bool) -> list:
        """
        Filters account summaries based on a given field and value.

        Args:
            filter_field (str): The field to filter on (e.g., 'balance', 'total_deposits', 'total_withdrawals').
            filter_value (int): The value to filter by.
            filter_mode (bool): A boolean indicating whether to filter records less than or equal to the value (True) or greater than or equal to the value (False).

        Returns:
            list: A list of filtered account summaries.
        """
        filtered_account_summaries = []
        for account_number, summary in self.__account_summaries.items():
            field_value = summary.get(filter_field, 0)

            if (filter_mode and field_value >= filter_value) or (not filter_mode and field_value <= filter_value):
                filtered_account_summaries.append({"Account number" : account_number ,"Balance": summary["balance"],
                                                   "Total Deposits" : summary["total_deposits"], "Total Withdrawals": summary["total_withdrawals"]}) 
                
                return filtered_account_summaries
            

def write_filtered_account_summaries_to_csv(self, filtered_data: list, file_path: str) -> None:
    """
    Write filtered account summaries to a CSV file.

    Args:
        filtered_data (list): A list of filtered account summaries.
        file_path (str): The file path where the CSV file will be saved.
    """
    with open(file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

        for summary in filtered_data:
            writer.writerow([
                summary['Account number'],
                summary['Balance'],
                summary['Total Deposits'],
                summary['Total Withdrawals']
            ])


           
                                             