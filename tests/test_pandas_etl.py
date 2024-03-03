#!/usr/bin/env python

"""Tests for `pandas_etl` package."""
from unittest.mock import patch

import pytest

from click.testing import CliRunner

from pandas_etl import simple_etl
from pandas_etl import runner


@pytest.fixture
def response():
    pass


def test_content(response):
    pass


@patch('pandas_etl.runner.SimpleETL', autospec=True)
@patch('pandas_etl.utils.file_util.load_yml')
def test_command_line_interface(mock_load_yml, mock_etl):
    """Test the CLI."""
    mock_etl_instance = mock_etl.return_value
    mock_load_yml.return_value = {}
    cli = CliRunner()
    args = ['--input_path', 'test_input', '--input_config_file', 'test_config', '--output_path', 'test_output_path']
    result = cli.invoke(runner.main, args=args, catch_exceptions=False)
    mock_etl.assert_called_once_with(input_path='test_input', input_config={},
                                     output_path='test_output_path', data_mapping_config={}, output_config={})
    mock_etl_instance.run.assert_called_once_with()
    assert result.exit_code == 0

