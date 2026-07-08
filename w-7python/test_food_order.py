import pytest
from food_order import calculate_total as food_order


def test_order1():
    assert food_order(10, 2) == 20


def test_order2():
    # test if total food order is equal to 30
    assert food_order(10, 3) == 30


def test_order3():
    # test if total food order is equal to 100
    assert food_order(20, 5) == 100


def test_order4():
    # test if total food order is equal to 10
    assert food_order(5, 2) == 10


def test_order5():
    # test if total food order is equal to "invalid price"
    with pytest.raises(ValueError):
        food_order(-5, 2)


def test_order6():
    # test if total food order is equal to "invalid quantity"
    with pytest.raises(ValueError):
        food_order(5, -2)