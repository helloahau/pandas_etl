from abc import ABC, abstractmethod


class ETL(ABC):
    """define the etl steps"""
    def __init__(self, input_paths, output_path):
        self.input_paths = input_paths
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
