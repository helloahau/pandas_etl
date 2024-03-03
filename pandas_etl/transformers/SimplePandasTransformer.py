from pandas_etl.transformers.transformer import Transformer
import pandas as pd


class SimplePandasTransformer(Transformer):
    def transform(self, df: pd.DataFrame):
        df.dropna(how='all', inplace=True)
        if self.rename_columns:
            df = df.rename(columns=self.rename_columns)
        if self.select_columns:
            df = df[self.select_columns]
        if self.fill_null:
            df = df.fillna(value=self.fill_null)
        if self.types:
            df = df.astype(self.types)
        return df
