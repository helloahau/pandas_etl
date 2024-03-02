"""Console script for pandas_etl."""
import sys
import click
import ast

from pandas_etl.simple_etl import SimpleETL


@click.command()
@click.option('--input_path')
@click.option('--input_config_file')
@click.option('--output_path')
def main(input_path, input_config_file, output_path):
    etl = SimpleETL(input_path=input_path, input_config_file = input_config_file, output_path=output_path)
    etl.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
