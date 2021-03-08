import socket

with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
	#set socket read timeout
	sock.settimeout(2)
	try:
		sock.sendall("ping".encode("utf-8"))
		data = sock.recv(1024).decode("utf-8")
		print(data)  
	except socket.timeout:
		print("send data timeout")
	except socket.error as ex:
		print('send data error ',ex)