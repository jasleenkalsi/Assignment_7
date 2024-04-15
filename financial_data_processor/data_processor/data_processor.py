class DataProcessor:
    """
    REQUIRED: CLASS DOCSTRING
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']

    def __init__(self, input_data: list):
        """
        REQUIRED: METHOD DOCSTRING
        """
        self.__input_data = input_data
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}

    @property
    def input_data(self):
        """
        REQUIRED: METHOD DOCSTRING
        """
        return self.__input_data
    
    @property
    def account_summaries(self):
        """
        REQUIRED: METHOD DOCSTRING
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self):
        """
        REQUIRED: METHOD DOCSTRING
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self):
        """
        REQUIRED: METHOD DOCSTRING
        """
        return self.__transaction_statistics


    def process_data(self) -> dict:
        """
        REQUIRED: METHOD DOCSTRING
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
        REQUIRED: METHOD DOCSTRING
        """
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        if account_number not in self.__account_summaries:
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, row: dict) -> None:
        """
        REQUIRED: METHOD DOCSTRING
        """
        amount = float(row['Amount'])
        currency = row['Currency']

        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(row)

    def update_transaction_statistics(self, row: dict) -> None:
        """
        REQUIRED: METHOD DOCSTRING
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        REQUIRED: METHOD DOCSTRING
        """
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]

        if transaction_count == 0:
            average = 0
        else:
            average = total_amount / transaction_count
        
        return average
