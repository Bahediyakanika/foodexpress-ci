from cart import cart_total


def test_cart_total():
    items = [
        {"price": 100, "qty": 2},
        {"price": 50, "qty": 1}
    ]

    assert cart_total(items) == 250


def test_empty_cart():
    items = []
    assert cart_total(items) == 0


def test_single_item():
    items = [
        {"price": 200, "qty": 3}
    ]

    assert cart_total(items) == 600