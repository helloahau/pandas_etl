from abc import abstractmethod, ABC


class Writer(ABC):
    def __init__(self, config):
        self.target_location = config.get('target_location')
        self.target_format = config.get('target_format')
        self.partition_cols = config.get('partition_cols', [])
        self.write_options = config.get('write_options', {})

    @abstractmethod
    def write(self, df, output_path):
        raise NotImplementedError("method not implemented in abstract class")