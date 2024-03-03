"""Console script for pandas_etl."""
import sys
import click
import ast

from pandas_etl.constant import INPUT_CONFIG_FILE, DATA_MAPPING_CONFIG, OUTPUT_CONFIG_FILE
from pandas_etl.simple_etl import SimpleETL
from pandas_etl.utils import file_util


@click.command()
@click.option('--input_path')
@click.option('--input_config_file', default=INPUT_CONFIG_FILE)
@click.option('--output_path')
@click.option('--data_mapping_config_file', default=DATA_MAPPING_CONFIG)
@click.option('--output_config_file', default=OUTPUT_CONFIG_FILE)
def main(input_path, input_config_file, output_path, data_mapping_config_file, output_config_file):
    input_config = file_util.load_yml(input_config_file)
    output_config = file_util.load_yml(output_config_file)
    data_mapping_config = file_util.load_yml(data_mapping_config_file)
    etl = SimpleETL(input_path=input_path, input_config=input_config, output_path=output_path,
                    data_mapping_config=data_mapping_config, output_config=output_config)
    etl.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
