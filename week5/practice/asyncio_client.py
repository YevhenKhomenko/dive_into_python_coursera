import asyncio

async def echo_client(message, loop):
	reader, writer = await asyncio.open_connection('127.0.0.1', 10001, loop=loop)

	print('send: {}'.format(message))
	writer.write(message.encode())
	writer.close()

loop = asyncio.get_event_loop()
message = 'hello'
loop.run_until_complete(echo_client(message, loop))
loop.close()