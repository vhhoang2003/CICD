import pytest
from src.warehouse import Warehouse

def test_add_product_valid():
    wh = Warehouse()
    wh.add_product("Laptop", 1000, 5)
    assert wh.inventory["Laptop"] == 5

def test_add_product_invalid():
    wh = Warehouse()
    with pytest.raises(ValueError):
        wh.add_product("Phone", -10, 5)