from pandas_etl.readers.csv_reader import CSVReader
from pandas_etl.readers.reader import Reader
from pandas_etl.writers.parquet_writer import ParquetWriter
from pandas_etl.writers.writer import Writer

READERS = {
    'csv': CSVReader,
}

WRITERS = {
    'parquet': ParquetWriter,
}


def get_reader(config) -> Reader:
    return READERS[config.get('data_format')](config)


def get_writer(config) -> Writer:
    return WRITERS[config.get('target_format')](config)
