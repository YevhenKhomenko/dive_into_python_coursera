class Value:
	def __init__(self):
		self.value = None

	@staticmethod
	def pay_commission(commission, value):
		return value * (1 - commission)

	def __get__(self, obj, obj_type):
		return self.value

	def __set__(self, obj, value):
		self.value = self.pay_commission(obj.commission, value)



class Account:
	amount = Value()

	def __init__(self, commission):
		self.commission = commission