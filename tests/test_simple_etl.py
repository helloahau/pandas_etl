from unittest.mock import patch

import pytest
import pandas as pd

from pandas_etl.constant import ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME
from pandas_etl.simple_etl import SimpleETL


class TestSimpleETL:
    @patch('pandas_etl.utils.file_util.load_yml')
    def test_validate(self, mock_load_yml):
        mock_load_yml.return_value = {'order': 'order.csv'}
        etl = SimpleETL('input_path', 'input_config_file', 'output_path')
        with pytest.raises(ValueError) as ve:
            etl.run()
        assert 'input dataset path must more than 2' in str(ve.value)

    @patch('pandas_etl.utils.file_util.load_yml')
    def test_extract(self, mock_load_yml):
        mock_load_yml.return_value = {ORDER_DATASET_NAME: {'data_path': 'order.csv', 'data_format': 'csv'},
                                      ORDER_ITEMS_DATASET_NAME: {'data_path': 'order_items.csv', 'data_format': 'csv'}}
        etl = SimpleETL('input_path', 'input_config_file', 'output_path')

        test_df = pd.DataFrame({'order_id': [1, 2, 3], 'item_id': [4, 5, 6]})

        with patch.object(pd, 'read_csv', side_effect=lambda filepath, dtype: test_df) as mock_read_csv:
            result = etl.extract()

            assert 2 == len(result)
            assert set(result.keys()) == {ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME}
            pd.testing.assert_frame_equal(result[ORDER_DATASET_NAME], test_df)
            pd.testing.assert_frame_equal(result[ORDER_ITEMS_DATASET_NAME], test_df)


