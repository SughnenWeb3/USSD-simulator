print("""
Welcome to Our Service🤗: 
Please Dial *555*78# to continue
""")
print()
ussd = "*555*78#"
balance = 1000

dialer = input("Enter USSD: ")
if dialer == ussd:
	print("""
Select the operation to carry out.
1. Buy Airtime
2. Buy Data
3. Borrow Airtime and Data
4. Check Balance
5. Stop
""")

	operation = int(input("Enter operation: "))
	#if operation <0 and operation >5:
	#print("Operation must be between 1-5")
	if operation == 1:
		airtime = float(input("Enter the amount to recharge: "))
		amt_to_recharge = balance - airtime
		if airtime > balance:
			print("Insufficient funds")		

		else:
			balance -= airtime
			print(f"You have recharged: {airtime} and your balance is: {balance}")
	elif operation == 2:
		print("""
		We have the following bundles
		1. 3GB = 1000
		2. 2GB = 750
		3. 1GB = 400 

		""")
		data = int(input("Select Data Bundle: "))
		if data == 1:
			rate = 1000
			if rate > balance:
				print("Your balance is low for this transaction")
			else:
				balance -= rate
				print("You have purchased 3GB of data at the rate of:",rate )
				print("Your balance is:", balance)
		elif data == 2:
			rate = 750
			if rate > balance:
				print("Your balance is low for this transaction")
			else:
				balance -= rate
				print("You have purchased 2GB of data at the rate of:", rate)
				print("Your balance is:", balance)
		elif data == 3:
			rate = 400
			if rate > balance:
				print("Your balance is low for this transaction")
			else:
				balance -= rate
				print("You have purchased 1GB of data at the rate of:", rate)
				print("Your balance is: ", balance)
		else:
			print("Selection Unavailable ❌")

	elif operation == 3:
		print("""
		Pick one below:
		1. Airtime
		2. Data
		""")
		option = int(input("Select choice: "))
		if option ==1:
		#	current_balance = 0
			air_borrow = float(input("Enter amount to borrow: "))
			if air_borrow > 1000:
				print("You cannot borrow above 1000")

			elif air_borrow >= 700 and air_borrow <=1000:
				percentage = 20
				current_balance = (percentage/100) * air_borrow
				new_balance = air_borrow - current_balance
				print(f"You have borrowed {air_borrow} and you have been charged {percentage}% and your current balance is {new_balance}")
			elif air_borrow >= 100 and air_borrow <= 650:
				percentage = 10
				current_balance = (percentage/100) * air_borrow
				new_balance = air_borrow - current_balance
				print(f"You have borrowed {air_borrow} and you have been charged {percentage}% and your current balance is {new_balance}")
			else:
				air_borrow <100
				print("You cannot borrow an amount less than 100")
		elif option ==2:
			print("""
			You are eligible to borrow the following
			1. 3GB = 1000
			2. 2GB = 700
			3. 1GB = 400
			""")
			data_to_borrow = int(input("Enter the bundle to borrow: "))
			if data_to_borrow == 1:
				rate = 1000
				percentage = 20
				refund = rate + (percentage/100)
				print(f"You have borrowed {data_to_borrow}GB of data and you have been charged {percentage}% and the amount to refund is {refund}")
			elif data_to_borrow ==2:
				rate = 700
				percentage = 10
				refund = rate + (percentage/100)
				print(f"You have borrowed {data_to_borrow}GB of data and you have been charged {percentage}% and the amount to refund is {refund}")

			elif data_to_borrow ==3:
				rate = 400
				percentage = 5
				refund = rate + (percentage/100)
				print(f"You have borrowed {data_to_borrow}GB of data and you have been charged {percentage}% and the amount to refund is {refund}")

			else:
				print("Option is unavailable")
	elif operation == 4:
		print(f"Your balance is {balance}")
	elif operation == 5:
		print("Thank you for using our services 🙏")
	else:
		print("Invalid Operation selected")
	

else:
	print("Invalid USSD")
