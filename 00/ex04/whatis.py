import sys

def is_odd(object: any):
	try:
		ret = int(object)
	except:
		raise AssertionError("argument is not an integer")
	if ret % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")

try:
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	elif len(sys.argv) == 1:
		print()
		exit(0)
	else:
		is_odd(sys.argv[1])
except Exception as e:
	print(e)
