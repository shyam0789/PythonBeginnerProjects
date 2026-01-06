class ShopManager:

    inventory = {
        "Apple": {"price": 1.2, "quantity": 50},
        "Banana": {"price": 0.5, "quantity": 100},
        "Milk": {"price": 2.5, "quantity": 20}
    }

    def add_product(self,product,price,quantity):
        self.inventory = {product: {price: quantity}}

    def update_quantity(self,product,quantity):
        self.inventory[product] = {"quantity":quantity}

    def show_inventory_report(self):
        print("")
        for prod,item in self.inventory.items():
            print(f"Prod: {prod}, Price :{item['price']}, Quantity: {item['quantity']}")

    def get_highest(self):

        highest_price_prod = [max(item['price']) for prod,item in self.inventory.items()]
        print(f"Highest Priced Product is: {highest_price_prod}")


shopMgr = ShopManager()
shopMgr.show_inventory_report()
shopMgr.get_highest()




