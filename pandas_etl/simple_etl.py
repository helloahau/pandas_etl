"""Main module."""
import pandas as pd

from pandas_etl.constant import ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME, PRODUCT_DATASET_NAME
from pandas_etl.etl import ETL


class SimpleETL(ETL):

    def validate(self):
        if not isinstance(self.input_paths, dict) or len(self.input_paths) < 2:
            raise ValueError('input dataset path must more than 2')

    def extract(self):
        dfs = {name: pd.read_csv(path) for name, path in self.input_paths.items()}
        return dfs

    # TODO: may need add more data type cast, column rename or agg logic
    def transform(self, dfs):
        df = dfs[ORDER_ITEMS_DATASET_NAME].merge(dfs[ORDER_DATASET_NAME], on='order_id', how='left')\
            .merge(dfs[PRODUCT_DATASET_NAME], on='product_id', how='left')
        return df

    def load(self, df):
        # TODO: should be better if using spark
        df.head(10).to_parquet(self.output_path, partition_cols=['product_id'])
