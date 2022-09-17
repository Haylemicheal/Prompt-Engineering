import pandas as pd
import json
class DataLoader:
    def read_xls(self, path):
        """A method for reading excel files
        Args:
            path: path of the file
        Returns:
            df: pandas data fream
        """
        df = pd.read_excel(path) 
        return df
    def read_json(self, path):
        """A method for reading json file
        Args:
            path: Path of the json file
        Returns:
            data: json file
        """
        with open(path) as f:
            data = json.load(f)
        return data
