'''
Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице.
Классы должны называться:
CarBase (базовый класс для всех типов машин),
Car (легковые автомобили),
Truck (грузовые автомобили)
SpecMachine (спецтехника).
Все объекты имеют обязательные атрибуты:
- car_type, значение типа объекта и может принимать одно из значений: «car», «truck», «spec_machine».
- photo_file_name, имя файла с изображением машины, допустимы расширения из списка: «.jpg», «.jpeg», «.png», «.gif»
- brand, марка производителя машины
- carrying, грузоподъемность (float)
'''




import csv
import os

class CarBase:
	'''
	Base class for all vehicle types
	'''
	def __init__(self, brand, photo_file_name, carrying):
		if os.path.splitext(photo_file_name)[1] not in [".jpg", ".jpeg", ".png", ".gif"]:
			raise ValueError("Wrong photo file name extension")
		self.carrying = float(carrying)
		self.brand = brand
		self.photo_file_name = photo_file_name
		
		

	def get_photo_file_ext(self):
		'''
		returns the extension of the foto
		'''
		return os.path.splitext(self.photo_file_name)[1]
		

class Car(CarBase):
	'''
	Car class
	'''
	car_type = 'car'

	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
	'''
	Truck class
	'''
	car_type = 'truck'
	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		whl = body_whl.split('x')										#TODO: check if all body_whl values are float
		try:
			if len(whl) > 3:
				raise ValueError("Invalid value for body_whl")

			self.body_width = float(whl[1])
			self.body_height = float(whl[2])
			self.body_length = float(whl[0])

		except (ValueError, IndexError):
				self.body_width = 0.0
				self.body_height = 0.0
				self.body_length = 0.0

	def get_body_volume(self):
		return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
	'''
	Special machine class
	'''
	car_type = 'spec_machine'

	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.extra = extra

def get_car_list(file_name):
	'''
	Reads from csv file, creates a vehicle object and a returns a list of vehicle objects.
	Restrictions for input:
	- 'carrying' must be float
	- 'photo_file_name' extension must be ".jpg", ".jpeg", ".png", ".gif"
	- 'passenger_seats_count' must be int
	- 'car_type' must be 'car', 'truck', 'spec_machine'
	'''
	car_list = []
	try:
		with open(file_name, 'r') as f:
			reader = csv.reader(f, delimiter = ';')
			next(reader)     
			for line in reader:
				try:
					car_type = line[0]
					brand = str(line[1])
					photo_file_name = str(line[3])
					carrying = float(line[5])

					if not(car_type and brand and photo_file_name and carrying):
						raise ValueError("Some required arguments are missing")
					if os.path.splitext(photo_file_name)[1] not in [".jpg", ".jpeg", ".png", ".gif"]:
						raise ValueError("Wrong photo file name extension")

					if car_type == 'car':
						passenger_seats_count = int(line[2])
						car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
					elif car_type == 'truck':
						body_whl = line[4]
						car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
					elif car_type == 'spec_machine':
						extra = line[6]
						if not extra:
							raise ValueError("Required argument extra is missing")
						car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
					else:
						raise ValueError("Wrong value for car_type")
				except (ValueError, IndexError):     #missing required arguments or arguments types are wrong
					continue

	except (FileNotFoundError, StopIteration):   #file was not found or file is empty
		return []        			 
	return car_list


if __name__ == '__main__':
	truck = Truck('brand', 'ph.jpg', 10, '3x4x5x6')
	print(truck.body_length)
	print(get_car_list("test.csv"))






		

