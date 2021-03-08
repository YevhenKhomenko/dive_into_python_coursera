import os
import tempfile

class File:
	def __init__(self, path_to_file):
		self.fp = None
		self.path_to_file = path_to_file
		if not os.path.exists(path_to_file):
			open(self.path_to_file, 'w').close()

	def read(self):
		with open(self.path_to_file, 'r') as file:
			text = file.read()
		return text

	def write(self, text):
		with open(self.path_to_file, 'w') as file:
			file.write(text)
		return len(text)

	def __str__(self):
		return os.path.abspath(self.path_to_file)

	def __add__(self, other):
		text = self.read() + other.read()
		new_file_obj = File(os.path.join(tempfile.gettempdir(), f'{hash(self) + hash(other)}.txt'))
		new_file_obj.write(text)
		return new_file_obj

	def __iter__(self):
		return self

	def __next__(self):
		if not self.fp:
			self.fp = open(self.path_to_file, 'r')
		line = self.fp.readline()
		if not line:
			self.fp.close()
			self.fp = None
			raise StopIteration
		return line
