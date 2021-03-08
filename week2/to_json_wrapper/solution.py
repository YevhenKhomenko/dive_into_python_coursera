from functools import wraps
import json

def to_json(func):
	@wraps(func)
	def inner(*args,**kwargs):
		return json.dumps(func(*args,**kwargs))
	return inner
