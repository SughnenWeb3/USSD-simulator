'''

students = {
   "S001": {"name": "John Doe", "age": 20, "score": 85},
    "S002": {"name": "Jane Smith", "age": 19, "score": 92},
    "S003": {"name": "Michael Brown", "age": 21, "score": 78},
   "S004": {"name": "Emily Davis", "age": 22, "score": 88},
   "S005": {"name": "Daniel Johnson", "age": 20, "score": 95},
    "S006": {"name": "Sarah Wilson", "age": 18, "score": 81},
   "S007": {"name": "David Lee", "age": 23, "score": 76}
   }

age = int(input("Enter age: "))
for student in students:
	if age == students[student]["age"]:
		print(students[student])
		break
		
		
	else:
		print("Not found")
		break
'''
'''
nums = [2,3,6,7,8,9,2,0]	
sec_num = int(input("Enter secret number: "))
for num in nums:
	if sec_num == num:
		print("You guessed correctly")
		break
	else:
		print("Ouch!")
		break
'''

nums = [2, 3, 6, 7, 8, 9, 2, 0]
sec_num = int(input("Enter secret number: "))

for num in nums:
    if sec_num == num:
	    print("You guessed correctly")
	    break
    else:
	    print("Ouch!")
	    break                                                                                                                                                                 

