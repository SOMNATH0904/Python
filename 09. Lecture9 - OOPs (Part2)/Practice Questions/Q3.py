'''
Ques: Create a class Order which stores item & its price.
      Use Dunder function __gt__() to convey that:
      order1 > order2 if price of order1 > price of order2
'''

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
    
order1 = Order("chips", 20)
order2 = Order("coffee", 15)

print("Is Price of Order1 > Order2 :",order1 > order2)