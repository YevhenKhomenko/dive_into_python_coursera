import asyncio

metrics_dict = {}

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        #self.metrics_dict = metrics_dict = {}

    def data_received(self, data):
    	#self.metrics_dict, resp = process_data(data.decode())
        resp = process_data(data.decode())
        self.transport.write(resp.encode())


def process_data(data):
	ok_msg = "ok\n\n"
	err_msg = "error\nwrong command\n\n"
	if data.strip("\n").strip() == "":
		return err_msg

	client_msg = data.split()
	command = client_msg[0]
	if command == "put":
		if len(client_msg) != 4:
			return err_msg

		try:
			metrics = client_msg[1]
			value = float(client_msg[2])
			timestamp = int(client_msg[3].strip("\n"))
		except ValueError:
			return err_msg

		if not metrics in metrics_dict:
			metrics_dict[metrics] = []
		for record_idx, record in enumerate(metrics_dict[metrics]):
			if record[0] == timestamp:
				metrics_dict[metrics][record_idx] = (timestamp, value)
				return ok_msg

		metrics_dict[metrics].append((timestamp, value))
		return ok_msg

	elif command == "get":
		if len(client_msg) != 2:
			return err_msg

		metrics = client_msg[1].strip("\n")
		if metrics == "*":
			response = "ok"
			for metr in metrics_dict:
				for record in metrics_dict[metr]:
					response += f"\n{metr} {record[1]} {record[0]}"
			response += "\n\n"
			return response

		if metrics not in metrics_dict:
			return ok_msg

		response = "ok"
		for record in metrics_dict[metrics]:
			response += f"\n{metrics} {record[1]} {record[0]}"
		response += "\n\n"
		return response

	else:
		return err_msg


def run_server(host, port):
	loop = asyncio.get_event_loop()
	coro = loop.create_server(
	    ClientServerProtocol,
	    host, port
	)

	server = loop.run_until_complete(coro)

	try:
	    loop.run_forever()
	except KeyboardInterrupt:
	    pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

if __name__ == '__main__':
	run_server('127.0.0.1', 8888)