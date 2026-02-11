def add(a,b):
	return a * b
def division(a, b):
	if b == 0:
		raise ValueError("sorry error")
	return a / b

print(add(30, 12))
print(division(10, 0))


