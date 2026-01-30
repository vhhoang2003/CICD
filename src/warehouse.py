class Warehouse:
    def __init__(self):
        self.inventory = {} # { "tên_sp": số_lượng }
        self.prices = {}    # { "tên_sp": giá_tiền }

    def add_product(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Giá và số lượng không được âm")
        self.inventory[name] = self.inventory.get(name, 0) + quantity
        self.prices[name] = price

    def calculate_total(self, cart, discount_code=None):
        """
        cart: { "tên_sp": số_lượng_mua }
        """
        total = 0
        for name, qty in cart.items():
            if name not in self.inventory or self.inventory[name] < qty:
                raise Exception(f"Sản phẩm {name} không đủ hàng!")
            total += self.prices[name] * qty
        
        # Áp dụng chiết khấu
        if discount_code == "GIAM10":
            total *= 0.9
        
        # Thuế VAT 10%
        return round(total * 1.1, 2)