"""Main module."""

from pandas_etl.constant import ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME, PRODUCT_DATASET_NAME
from pandas_etl.etl import ETL
from pandas_etl.readers.reader import Reader
from pandas_etl.utils import reader_util


class SimpleETL(ETL):

    def validate(self):
        if not isinstance(self.input_config, dict) or len(self.input_config) < 2:
            raise ValueError('input dataset path must more than 2')

    def extract(self):
        dfs = {name: reader_util.get_reader(config).read(self.input_path) for name, config in self.input_config.items()}
        return dfs

    # TODO: may need add more data type cast, column rename or agg logic
    def transform(self, dfs):
        df = dfs[ORDER_ITEMS_DATASET_NAME].merge(dfs[ORDER_DATASET_NAME], on='order_id', how='left')\
            .merge(dfs[PRODUCT_DATASET_NAME], on='product_id', how='left')
        return df

    def load(self, df):
        # should be better if using spark
        df.head(10).to_parquet(self.output_path, partition_cols=['product_id'])
