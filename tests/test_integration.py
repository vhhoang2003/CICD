from src.warehouse import Warehouse
def test_purchase_flow():
    wh = Warehouse()
    wh.add_product("Mouse", 20, 10)
    wh.add_product("Keyboard", 50, 5)
    
    cart = {"Mouse": 2, "Keyboard": 1}
    # (20*2 + 50*1) = 90. Giảm 10% còn 81. Thuế 10% của 81 = 8.1. Tổng = 89.1
    total = wh.calculate_total(cart, discount_code="GIAM10")
    assert total == 89.1