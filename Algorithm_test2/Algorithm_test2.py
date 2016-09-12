validCharacters = {"1":"`", "2":"1", "3":"2", "4":"3", "5":"4", "6":"5", "7":"6", "8":"7", "9":"8", "0":"9", "-":"0", "=":"-"
, "W":"Q", "E":"W", "R":"E", "T":"R", "Y":"T", "U":"Y", "I":"U", "O":"I", "P":"O", "[":"P", "]":"[", "\\":"]"
, "S":"A", "D":"S", "F":"D", "G":"F", "H":"G", "J":"H", "K":"J", "L":"K", ";":"L", "'":";"
, "X":"Z", "C":"X", "V":"C", "B":"V", "N":"B", "M":"N", ",":"M", ".":",", "/":"."}

def isInvalidString(inputString):
	invalidation=False

	for part in getStringSplits(inputString):
		for char in getSingleCharacters(part):
			if char in validCharacters:
				invalidation=False
			else:
				invalidation=True
				return invalidation
	return invalidation

def getStringSplits(str):
	return str.split()

def getSingleCharacters(str):
	return list(str)

def correctString(inputString):
	correction = ""

	for part in getStringSplits(inputString):
		for char in getSingleCharacters(part):
			correction = correction + validCharacters.get(char)
		correction = correction + " "
	print(correction)
	

while True:
	try:
		inputString = input()
		if isInvalidString(inputString):
			raise ValueError
	except ValueError:
		print("ValueError")
	else:
		correctString(inputString)