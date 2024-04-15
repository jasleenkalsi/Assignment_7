import os

from input_handler.input_handler import InputHandler
from data_processor.data_processor import DataProcessor
from output_handler.output_handler import OutputHandler

def main() -> None:
    """Main function to read input data, process it, and write the results to output files.

    - Reads input data from a CSV file using InputHandler.
    - Processes the data using DataProcessor.
    - Writes the processed data to CSV and JSON files using OutputHandler.
    """

    # Retrieves the directory name of the current script or module file.
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Joins the current directory, the relative path to the input folder and the filename 
    # to create a complete path to the file.
    input_file_path = os.path.join(current_dir, 'input\\input_data.csv')

    input_handler = InputHandler(input_file_path)
    input_data = input_handler.read_input_data()

    data_processor = DataProcessor(input_data)
    processed_data = data_processor.process_data()

    output_file_prefix = 'output_data'
    output_handler = OutputHandler(processed_data['account_summaries'], processed_data['suspicious_transactions'], processed_data['transaction_statistics'])


    # Joins the current directory, the relative path to the output folder and the filename 
    # to create a complete path to each of the output files.
    account_summaries_file = os.path.join(current_dir,f'output\\{output_file_prefix}_account_summaries.csv')
    suspicious_transactions_file = os.path.join(current_dir,f'output\\{output_file_prefix}_suspicious_transactions.csv')
    transaction_statistics_file = os.path.join(current_dir,f'output\\{output_file_prefix}_transaction_statistics.csv')


    output_handler.write_account_summaries_to_csv(account_summaries_file)
    output_handler.write_suspicious_transactions_to_csv(suspicious_transactions_file)
    output_handler.write_transaction_statistics_to_csv(transaction_statistics_file)

if __name__ == '__main__':
    main()
