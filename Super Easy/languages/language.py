from sys import stdin
case = 0
while True:
	hello = stdin.readline()
	hello = hello.strip()
	case += 1
	if hello == "#":
		break
	else:
		
		print("Case ", end = "")
		print(case, end = "")
		print(": ", end = "")
		if hello == "HELLO":
			print("ENGLISH")
		elif hello == "HOLA":
			print("SPANISH")
		elif hello == "HALLO":
			print("GERMAN")
		elif hello == "BONJOUR":
			print("FRENCH")
		elif hello == "CIAO":
			print("ITALIAN")
		elif hello == "ZDRAVSTVUJTE":
			print("RUSSIAN")
		else:
			print("UNKNOWN")		