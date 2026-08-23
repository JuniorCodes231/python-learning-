while True:

	num1 = int(input("enter first number"))
	num2 = int(input("enter second 	number"))
	operation = input(" - + / * ")
	
	if operation == "-":
			answer = num1- num2
	elif operation == "+":
			answer = num1+ num2
	elif operation == "*":
			answer = num1*num2
	elif operation == "/":
			answer = num1/num2
	else:
			print("invalid")
			answer = 0
	print("answer" ,answer)
