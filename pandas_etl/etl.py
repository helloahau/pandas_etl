from abc import ABC, abstractmethod


class ETL(ABC):
    """define the etl steps"""
    def __init__(self, input_path, input_config, output_path, data_mapping_config, output_config):
        self.input_path = input_path
        self.input_config = input_config
        self.output_path = output_path
        self.data_mapping_config = data_mapping_config
        self.output_config = output_config

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
