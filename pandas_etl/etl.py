from abc import ABC, abstractmethod

from pandas_etl.utils import file_util


class ETL(ABC):
    """define the etl steps"""
    def __init__(self, input_path, input_config_file, output_path):
        self.input_path = input_path
        self.input_config = file_util.load_yml(input_config_file)
        self.output_path = output_path

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, dfs):
        pass

    @abstractmethod
    def load(self, df, file_path):
        pass

    def run(self):
        self.validate()
        dfs = self.extract()
        df = self.transform(dfs)
        self.load(df)
