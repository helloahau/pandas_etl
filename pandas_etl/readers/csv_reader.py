from pandas_etl.readers.reader import Reader
import pandas as pd


class CSVReader(Reader):
    def read(self, path):
        return pd.read_csv(path + '/' + self.data_path, **self.read_options, dtype=self.schema)
