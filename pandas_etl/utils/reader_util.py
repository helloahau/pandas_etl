from pandas_etl.readers.csv_reader import CSVReader

READERS = {
    "csv": CSVReader,
}


def get_reader(config):
    return READERS[config.get("data_format")](config)
