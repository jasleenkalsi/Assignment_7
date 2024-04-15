import csv
import json

class InputHandler:
    """
    REQUIRED: CLASS DOCSTRING
    """
    def __init__(self, file_path: str):
        """
        REQUIRED: METHOD DOCSTRING
        """
        self.__file_path = file_path

    @property
    def file_path(self):
        """
        REQUIRED: METHOD DOCSTRING
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """
        REQUIRED: METHOD DOCSTRING
        """
        return self.__file_path.split('.')[-1]

    def read_input_data(self) -> list:
        """
        REQUIRED: METHOD DOCSTRING
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data =  self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()
        return data

    def read_csv_data(self) -> list:
        """
        REQUIRED: METHOD DOCSTRING
        """
        input_data = []
        try:
            with open(self.__file_path, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    input_data.append(row)
            return input_data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        

    def read_json_data(self) -> list:
        """
        REQUIRED: METHOD DOCSTRING
        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        try:

            with open(self.__file_path, 'r') as input_file:
                input_data = json.load(input_file)

            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")
