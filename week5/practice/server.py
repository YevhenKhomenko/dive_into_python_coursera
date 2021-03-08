import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind('127.0.0.1', 10001)
	sock.listen()
	while True:
		conn, addr = sock.accept()
		conn.settimeout(5)
		with conn:
			while True:
				try:
					data = conn.recv(1024)
				except socket.timeout:
					print("close connection by timeout")
					break


				print(data.decode("utf-8"))
