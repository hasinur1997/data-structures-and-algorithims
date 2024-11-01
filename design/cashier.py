class Cashier:

    def __init__(self, n, discount, products, prices):
        self.nth = n
        self.order_counter = 1
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, product, amount) -> float:
        subtotal = 0

        for i in range(len(product)):
            product_id = product[i]
            index = self.products.index(product_id)
            price = self.prices[index]
            quantity = amount[i]
            subtotal += price * quantity

        if self.order_counter == self.nth:
            subtotal = subtotal * ((100 - self.discount) / 100)
            self.order_counter = 1
        else:
            self.order_counter += 1

        return round(float(subtotal), 1)


cashier = Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100])

print(cashier.getBill([1, 2], [1, 2]))
print(cashier.getBill([3,7],[10,10]))
print(cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]))
print(cashier.getBill([4],[10]))
print(cashier.getBill([7,3],[10,10]))
print(cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]))
print(cashier.getBill([2,3,5],[5,3,2]))