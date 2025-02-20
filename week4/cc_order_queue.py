class Queue:
	def __init__(self):
		self.items = []
	
	def size(self):
		return len(self.items)
	
	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		if self.size() == 0:
			return None
		return self.items.pop(0)
	
	def show_queue(self):
		print(self.items)

class IceCreamShop:
	def __init__(self, flavors):
		self.flavors = flavors
		self.orders = Queue()

	def take_order(self, customer: str, flavor: str, scoops: int):
		if flavor not in self.flavors or scoops < 1 or scoops > 3:
			print("ERROR: Flavor doesn't exist OR number of scoops out of range.")
			return
		else:
			print("Order created.")

		order = {
			"customer": customer,
			"flavor": flavor,
			"scoops": scoops
			}
		
		self.orders.enqueue(order)
			
	def show_all_orders(self):
		print("\nAll Pending Ice Cream Orders:")
		for order in self.orders.items:
			print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")

	def next_order(self):
		print("\nNext Order Up!")

		next_order = self.orders.dequeue()
		print(f"Customer: {next_order['customer']} -- Flavor: {next_order['flavor']} -- Scoops: {next_order['scoops']}")


# TEST

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()