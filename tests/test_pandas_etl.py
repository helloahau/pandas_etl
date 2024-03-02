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
def test_command_line_interface(mock_etl):
    """Test the CLI."""
    mock_etl_instance = mock_etl.return_value
    cli = CliRunner()
    args = ['--input_path', 'test_input', '--input_config_file', 'test_config', '--output_path', 'test_output_path']
    result = cli.invoke(runner.main, args=args, catch_exceptions=False)

    mock_etl.assert_called_once_with(input_path='test_input', input_config_file='test_config',
                                     output_path='test_output_path')
    mock_etl_instance.run.assert_called_once_with()
    assert result.exit_code == 0

