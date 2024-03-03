from pandas_etl.writers.writer import Writer


class ParquetWriter(Writer):
    def write(self, df, output_path):
        df.head(10).to_parquet(output_path + '/' + self.target_location, **self.write_options,
                               partition_cols=self.partition_cols)
