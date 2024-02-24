"""Console script for pandas_etl."""
import sys
import click
import ast

from pandas_etl.simple_etl import SimpleETL


@click.command()
@click.option('--input_paths')
@click.option('--output_path')
def main(input_paths, output_path):
    input_paths_dict = ast.literal_eval(input_paths)
    etl = SimpleETL(input_paths=input_paths_dict, output_path=output_path)
    etl.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
