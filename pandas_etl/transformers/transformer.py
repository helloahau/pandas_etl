from abc import ABC, abstractmethod


class Transformer(ABC):
    def __init__(self, config):
        self.config = config
        self.rename_columns = self.config.get('rename_columns')
        self.select_columns = self.config.get('select_columns')
        self.fill_null = self.config.get('fill_null')
        self.types = self.config.get('types', {})

    @abstractmethod
    def transform(self):
        raise NotImplementedError("method not implemented in abstract class")
