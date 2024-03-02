import json
from abc import ABC, abstractmethod
from typing import Dict


class Reader(ABC):

    def __init__(self, config):
        self.config = config
        self._validate_config()
        self.read_options: Dict[str, str] = self.config.get("read_options", {})
        self.data_path = self.config["data_path"]
        self.data_format = self.config.get("data_format")
        self.schema = self.config.get("schema", None)

    def _validate_config(self):
        """ validate the config fields """
        pass

    @abstractmethod
    def read(self, path):
        raise NotImplementedError("method not implemented in abstract class")

