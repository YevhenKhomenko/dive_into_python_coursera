def coroutine(func):
	def start_coroutine(*args, **kwargs):
		cr = func(*args, **kwargs)
		next(cr) #cr.send(None)
		return cr
	return start_coroutine

@coroutine
def grep(pattern):
	print('start grep')
	try:
		while True:
			line = yield
			if pattern in line:
				print(line)
	except GeneratorExit:
		print('stop grep')

@coroutine
def grep_python_coroutine():
	g = grep('python') 
	yield from g

g = grep('python')
#next(g) #g.send(None)
g.send("php is better")
g.send("python is simplier")
g.close()