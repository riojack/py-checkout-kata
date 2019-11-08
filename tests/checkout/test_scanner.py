import math
from unittest.mock import patch, call

from src.checkout.scanner import Scanner


class TestScanner:
    def setup_method(self):
        # noinspection PyAttributeOutsideInit
        self.price_model_patcher = patch('src.checkout.price_model.PriceModel')
        self.price_model = self.price_model_patcher.start()

    def teardown_method(self):
        self.price_model_patcher.stop()

    def test_should_calculate_total_by_querying_pricing_model(self):
        self.price_model.look_up_product.return_value = 1.55
        total = Scanner(self.price_model) \
            .scan('orange') \
            .total()

        self.__assert_called_with(self.price_model.look_up_product, 'orange')
        assert total == 1.55

    def test_scan_should_return_itself(self):
        self.price_model.look_up_product.return_value = 1.55
        scanner = Scanner(self.price_model)

        assert scanner.scan('orange') == scanner

    def test_should_query_pricing_model_for_each_item_scanned(self):
        self.price_model.look_up_product.side_effect = [0.70, 2.87, 1.95]
        total = Scanner(self.price_model) \
            .scan('kiwi') \
            .scan('pineapple') \
            .scan('loaf of bread') \
            .total()

        self.__assert_called_with(self.price_model.look_up_product, 'kiwi')
        self.__assert_called_with(self.price_model.look_up_product, 'pineapple')
        self.__assert_called_with(self.price_model.look_up_product, 'loaf of bread')
        assert math.isclose(total, 5.52, rel_tol=0.00001)

    def test_items_scanned_should_return_a_list_of_the_items_scanned(self):
        items_scanned = Scanner(self.price_model) \
            .scan('kiwi') \
            .scan('kiwi') \
            .scan('spaghetti') \
            .items_scanned()

        assert items_scanned.count('kiwi') == 2
        assert 'spaghetti' in items_scanned

    @staticmethod
    def __assert_called_with(mock_calls, call_argument):
        assert call(call_argument) in mock_calls.call_args_list
