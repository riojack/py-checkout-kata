from src.checkout.price_model import PriceModel, sold_by_unit


def test_should_save_product_as_sold_by_unit_by_default():
    model = PriceModel() \
        .add_product('stick of gum', 0.95)

    assert model.look_up_product('stick of gum') == (0.95, sold_by_unit())


def test_should_save_and_load_product_information_for_multiple_products():
    model = PriceModel() \
        .add_product('candy bar', 0.85) \
        .add_product('carrot', 0.15) \
        .add_product('peanuts', 3.25)

    assert model.look_up_product('candy bar') == (0.85, sold_by_unit())
    assert model.look_up_product('carrot') == (0.15, sold_by_unit())
    assert model.look_up_product('peanuts') == (3.25, sold_by_unit())


def test_should_return_price_of_zero_as_sold_by_unit_if_product_not_found():
    model = PriceModel()

    assert model.look_up_product('apple') == (0.0, sold_by_unit())


def test_should_overwrite_product_if_the_same_product_is_added_multiple_times():
    model = PriceModel() \
        .add_product('orange', 0.65) \
        .add_product('orange', 0.58) \
        .add_product('orange', 0.53)

    assert model.look_up_product('orange') == (0.53, sold_by_unit())
