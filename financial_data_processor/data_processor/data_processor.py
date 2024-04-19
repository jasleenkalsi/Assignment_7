class DataProcessor:
    """
    A class for processing financial transaction data.
    Attributes:
        LARGE_TRANSACTION_THRESHOLD (int): Threshold for identifying large transactions.
        UNCOMMON_CURRENCIES (list): List of uncommon currencies for identifying suspicious transactions.
    Methods:
        __init__: Initializes a DataProcessor object.
        process_data: Processes the input data and returns processed information.
        update_account_summary: Updates account summaries based on transaction data.
        check_suspicious_transactions: Checks for suspicious transactions.
        update_transaction_statistics: Updates transaction statistics based on transaction data.
        get_average_transaction_amount: Calculates the average transaction amount for a given transaction type.
    """
    LARGE_TRANSACTION_THRESHOLD = 10000  
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']  
    def __init__(self, input_data: list):
        """
        Initializes a DataProcessor object.
        Args:
            input_data (list): List of dictionaries containing transaction data.
        """
        self.__input_data = input_data
        self.__account_summaries = {}  
        self.__suspicious_transactions = []  
        self.__transaction_statistics = {}  
    @property
    def input_data(self):
        """
        Returns the input data.
        Returns:
            list: List of dictionaries containing transaction data.
        """
        return self.__input_data
    @property
    def account_summaries(self):
        """
        Returns the account summaries.
        Returns:
            dict: Dictionary containing account summaries.
        """
        return self.__account_summaries
    @property
    def suspicious_transactions(self):
        """
        Returns the suspicious transactions.
        Returns:
            list: List of dictionaries containing suspicious transactions.
        """
        return self.__suspicious_transactions
    @property
    def transaction_statistics(self):
        """
        Returns the transaction statistics.
        Returns:
            dict: Dictionary containing transaction statistics.
        """
        return self.__transaction_statistics
    def process_data(self) -> dict:
        """
        Processes the input data and returns processed information.
        Returns:
            dict: Processed information including account summaries, suspicious transactions, and transaction statistics.
        """
        for row in self.__input_data:
            self.update_account_summary(row)
            self.check_suspicious_transactions(row)
            self.update_transaction_statistics(row)
        return {
            "account_summaries": self.__account_summaries,
            "suspicious_transactions": self.__suspicious_transactions,
            "transaction_statistics": self.__transaction_statistics
        }
    def update_account_summary(self, row: dict) -> None:
        """
        Updates account summaries based on transaction data.
        Args:
            row (dict): Dictionary containing transaction data.
        """
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])
        # Initialize account summary if not already present
        if account_number not in self.__account_summaries:
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }
        # Update account balance and transaction amounts
        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount
    def check_suspicious_transactions(self, row: dict) -> None:
        """
        Checks for suspicious transactions.
        Args:
            row (dict): Dictionary containing transaction data.
        """
        amount = float(row['Amount'])
        currency = row['Currency']
        # Check for large transactions or uncommon currencies
        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(row)
    def update_transaction_statistics(self, row: dict) -> None:
        """
        Updates transaction statistics based on transaction data.
        Args:
            row (dict): Dictionary containing transaction data.
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])
        # Initialize transaction statistics if not already present
        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }
        # Update transaction statistics
        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1
    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Calculates the average transaction amount for a given transaction type.
        Args:
            transaction_type (str): Type of transaction.
        Returns:
            float: Average transaction amount.
        """
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]
        # Calculate average transaction amount
        if transaction_count == 0:
            average = 0
        else:
            average = total_amount / transaction_count
        return average