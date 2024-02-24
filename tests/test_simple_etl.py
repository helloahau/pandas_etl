from unittest.mock import patch

import pytest
import pandas as pd

from pandas_etl.constant import ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME
from pandas_etl.simple_etl import SimpleETL


class TestSimpleETL:
    def test_validate(self):
        etl = SimpleETL('input_paths', 'output_path')
        with pytest.raises(ValueError) as ve:
            etl.run()
        assert 'input dataset path must more than 2' in str(ve.value)

    def test_extract(self):
        etl = SimpleETL({ORDER_DATASET_NAME: 'order.csv', ORDER_ITEMS_DATASET_NAME: 'order_items.csv'}, 'output_path')

        test_df = pd.DataFrame({'order_id': [1, 2, 3], 'item_id': [4, 5, 6]})

        with patch.object(pd, 'read_csv', side_effect=lambda filepath: test_df) as mock_read_csv:
            result = etl.extract()

            mock_read_csv.assert_any_call('order.csv')
            mock_read_csv.assert_any_call('order_items.csv')

            assert 2 == len(result)
            assert set(result.keys()) == {ORDER_DATASET_NAME, ORDER_ITEMS_DATASET_NAME}
            pd.testing.assert_frame_equal(result[ORDER_DATASET_NAME], test_df)
            pd.testing.assert_frame_equal(result[ORDER_ITEMS_DATASET_NAME], test_df)


