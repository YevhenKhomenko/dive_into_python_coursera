
class FileReader:

	def __init__(self, file_path = None):
		self.path = file_path

	def read(self):
		try:
			with open(f'{self.path}', 'r') as f:
				text = f.read()
		except FileNotFoundError:
			return ''
		else:
			return text

#reader = FileReader("file.txt")
#print(reader.read())


