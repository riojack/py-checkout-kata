from checkout.price_model import PriceModel


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
