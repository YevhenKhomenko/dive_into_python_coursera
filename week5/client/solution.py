import socket
import time

class ClientError(Exception):
	'''
	Exception raised for general network errors
	'''
	def __init__(self, message):
		self.message = message
		Exception.__init__(self, f'ClientError: {message}')

class Client:
	def __init__(self, host, port, timeout = None):
		'''
		Creating connection with server.
		'''
		self.host = host
		self.port = port
		self.timeout = timeout
		try:
			self.sock = socket.create_connection((host,port),timeout)
			self.sock.settimeout(timeout)
		except OSError:
			self.sock.close()
			raise ClientError('Failed to connect to server.')

	def put(self, key, value, timestamp = None):
		'''
		Sending data to server in format: 'put <key> <value> <timestamp>',
		response should be either 'ok\n\n' or 'error\nwrong command\n\n'
		'''
		try:
			if not timestamp:
				self.sock.sendall(f'put {key} {value} {int(time.time())}\n'.encode('utf-8'))
			else:
				self.sock.sendall(f'put {key} {value} {timestamp}\n'.encode('utf-8'))
			response = self.sock.recv(1024).decode('utf-8')
			if response.split('\n')[0] == 'error':
				raise ClientError('Wrong command.')

		except OSError:
			self.sock.close()
			raise ClientError('Failed to send data to server.')

	def get(self, key):
		'''
		Getting data from server. Request format: 'get <key>\n'.
		Response format:  '<status>\n<data>\n\n'
		'''
		data_dict = {}
		try:
			self.sock.sendall(f'get {key}\n'.encode('utf-8'))
			response = self.sock.recv(1024).decode('utf-8')
			response_list = response.split('\n')
			status = response_list[0]
			if status == 'ok':
				data = response_list[1:-2]
				for record in data:
					record = record.split(' ')
					if record[0] not in data_dict:
						data_dict[record[0]] = []
					data_dict[record[0]].append((int(record[2]), float(record[1])))
					data_dict[record[0]].sort(key = lambda tup: tup[0])
			else:
				raise ClientError('Wrong command.')

		except OSError:
			self.sock.close()
			raise ClientError('Failed to get data from server.')
		except (IndexError,ValueError):
			self.sock.close()
			raise ClientError('Incorrect response from server.')

		return data_dict



