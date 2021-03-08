import asyncio

#@asyncio.coroutine  -deprecated , use async def instead
async def hello_world():
	while True:
		print('Hello world')
		#yield from asyncio.sleep(1.0) - deprecated
		await asyncio.sleep(1.0) 

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()