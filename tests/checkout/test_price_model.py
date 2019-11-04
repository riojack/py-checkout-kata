from src.checkout.price_model import PriceModel


def test_should_save_and_load_pricing_information():
    model = PriceModel() \
        .add('candy bar', 0.85) \
        .add('carrot', 0.15) \
        .add('peanuts', 3.25)

    assert model.look_up_price('candy bar') == 0.85
    assert model.look_up_price('carrot') == 0.15
    assert model.look_up_price('peanuts') == 3.25


def test_should_return_zero_if_product_not_found():
    model = PriceModel()

    assert model.look_up_price('apple') == 0.0


def test_should_overwrite_product_if_the_same_product_is_added_multiple_times():
    model = PriceModel() \
        .add('orange', 0.65) \
        .add('orange', 0.58) \
        .add('orange', 0.53)

    assert model.look_up_price('orange') == 0.53
