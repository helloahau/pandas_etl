"""Main module."""

from pandas_etl.constant import ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME, PRODUCT_DATASET_NAME, \
    ORDER_PURCHASE_TIME_COL, DATE_TIME_FORMAT
from pandas_etl.etl import ETL
from pandas_etl.transformers.SimplePandasTransformer import SimplePandasTransformer
from pandas_etl.utils import etl_util
import pandas as pd


class SimpleETL(ETL):

    def validate(self):
        if not isinstance(self.input_config, dict) or len(self.input_config) < 2:
            raise ValueError('input dataset path must more than 2')

    def extract(self):
        dfs = {name: etl_util.get_reader(config).read(self.input_path) for name, config in self.input_config.items()}
        return dfs

    def transform(self, dfs):
        """do transformation by data type cast, column rename or agg logic"""
        dfs = {name: SimplePandasTransformer(self.data_mapping_config.get(name, {})).transform(df) for name,
                                                                            df in dfs.items()}
        order_df = dfs[ORDER_DATASET_NAME]
        order_df[ORDER_PURCHASE_TIME_COL] = pd.to_datetime(order_df[ORDER_PURCHASE_TIME_COL], format=DATE_TIME_FORMAT)

        order_items_df = dfs[ORDER_ITEMS_DATASET_NAME]
        product_df = dfs[PRODUCT_DATASET_NAME]

        df = order_df.merge(order_items_df, on='order_id', how='left').merge(product_df, on='product_id', how='left')
        return df

    def load(self, df):
        etl_util.get_writer(self.output_config.get('simple_etf')).write(df, self.output_path)
