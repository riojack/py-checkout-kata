from unittest.mock import patch

from src.checkout.scanner import Scanner


class TestScanner:
    def setup_method(self):
        # noinspection PyAttributeOutsideInit
        self.price_model_patcher = patch('src.checkout.price_model.PriceModel')
        self.price_model = self.price_model_patcher.start()

    def teardown_method(self):
        self.price_model_patcher.stop()

    def test_should_calculate_total_by_querying_pricing_model(self):
        self.price_model.look_up_price.return_value = 1.55
        scanner = Scanner(self.price_model)
        scanner.scan('orange')
        total = scanner.total()

        self.__assert_called_with(self.price_model.look_up_price, 'orange')
        assert total == 1.55

    def test_scan_should_return_itself(self):
        self.price_model.look_up_price.return_value = 1.55
        scanner = Scanner(self.price_model)

        assert scanner.scan('orange') == scanner
    @staticmethod
    def __assert_called_with(mock_calls, arg1):
        assert mock_calls.call_args == [(arg1,)]
