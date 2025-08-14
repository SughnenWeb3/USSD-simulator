'''
numbers = [12,75,150,180,145,525,50]

for number in numbers:
	#if number % 5 == 0:
		#print(number)
	if number > 500:
		break
	if number > 150:
		continue
	if number % 5 ==0:
		print(number)
else:
	pass
'''
'''
numbers = [12, 75, 150,180,145,525,50]	
largest = numbers[0]
for number in numbers:
	if number > largest:
		largest = number 
	#count = max(numbers)
print("The largest number is: ",largest)
#to print the smallest number, simply change the comparison operator
'''
'''
record = []
for _ in range(0,3):
	name = input("Enter your name: ")
	score = float(input("Enter score: "))
	level = int(input("Enter level: "))
	while True:
		gender = input("Enter gender: ").capitalize()
		if gender == "M":
			break
		elif gender == "F":
			break
		else:
			print("You must type (M/F)")

#for _ in range(0,3):

	student = {
	"name": name,
	"score":score,
	"level":level,
	"gender":gender
		}
	record.append(student)
	
'''

'''
orders = [
    {"order_id": 101, "customer": "John", "items": 3, "total_price": 75},
    {"order_id": 102, "customer": "Mary", "items": 10, "total_price": 180},
    {"order_id": 103, "customer": "Alex", "items": 2, "total_price": 50},
    {"order_id": 104, "customer": "Grace", "items": 15, "total_price": 600},
    {"order_id": 105, "customer": "Paul", "items": 5, "total_price": 145}
]
'''
'''
Task:
1. Print the customer name and total_price for orders with 5 or more items.
2. Skip orders with total_price between 140 and 200.
3. If any total_price is greater than 500, stop the loop.
'''
'''
for order in orders:
    if order["total_price"] > 500:
	    #print("The customer is",order['customer'], "and  has total_price", order['total_price'])
	    break
    
   # if order["items"] >= 5:
	   # print(order["items"])
    if  order["total_price"]>= 140 and order["total_price"] <= 200:
	    #print("The customer", order['customer'], "total_price",  order['total_price'])
	    continue
    if order["items"]>=5:
	    print(f"{order['customer']}, Total Price: {order['total_price']}")

'''
'''
posts = [
    {"post": {"greeting": "Welcome"}},
    {"post": {"greeting": "Hello"}},
    {"post": {"greeting": "Come"}}
]

for post in posts:
	if post["post"]["greeting"]=="Welcome":
		print(posts["post"])


'''
'''

students = {
    "S001": {"name": "John Doe", "age": 20, "score": 85},
    "S002": {"name": "Jane Smith", "age": 19, "score": 92},
    "S003": {"name": "Michael Brown", "age": 21, "score": 78},
    "S004": {"name": "Emily Davis", "age": 22, "score": 88}
}
for student in students:
	print(students[student]["name"])
	'''
	'''
	if students[student]["name"] == "Jane Smith":
		print(f"The name of the student is: {students[student]['name']}")
		break
	if students[student]["score"]==85:
		print(f"The score of the student is: {students[student]['score']}")
else:
	print("Invalid")
'''
'''
students = [
    {"name": "John Doe", "age": 20, "score": 85},
    {"name": "Jane Smith", "age": 19, "score": 92},
    {"name": "Michael Brown", "age": 21, "score": 78},
    {"name": "Emily Davis", "age": 22, "score": 88},
    {"name": "David Wilson", "age": 20, "score": 81}
]

for student in students:
	if student["score"]<= 50:
		print(student["score"])
else:
	print("Not found")
'''
'''
students = [
    {
        "name": "John Doe",
        "age": 20,
        "score": 85,
        "gender": "Male",
        "level": "200",
        "subjects": ["Math", "Physics", "Computer Science"],
        "address": {"city": "Lagos", "country": "Nigeria"}
    },
    {
        "name": "Jane Smith",
        "age": 19,
        "score": 92,
        "gender": "Female",
        "level": "100",
        "subjects": ["Biology", "Chemistry", "English"],
        "address": {"city": "Abuja", "country": "Nigeria"}
    },
    {
        "name": "Michael Brown",
        "age": 21,
        "score": 78,
        "gender": "Male",
        "level": "300",
        "subjects": ["Economics", "Statistics", "Accounting"],
        "address": {"city": "Kano", "country": "Nigeria"}
    },
    {
        "name": "Emily Davis",
        "age": 22,
        "score": 88,
        "gender": "Female",
        "level": "400",
        "subjects": ["Law", "Political Science", "History"],
        "address": {"city": "Ibadan", "country": "Nigeria"}
    },
    {
        "name": "David Wilson",
        "age": 20,
        "score": 81,
        "gender": "Male",
        "level": "200",
        "subjects": ["Philosophy", "Psychology", "Sociology"],
        "address": {"city": "Port Harcourt", "country": "Nigeria"}
    }
]

for student in students:
	print(student["subjects"])
	
	
else:
	pass	
'''
'''
mum = [1,2,3,4,5,6,7]
for num in mum:
	if num >=3 and num <=6:
		print(num)
'''
'''
student_DB = {"name": "Tom", "age":20, "gender": "Male", "score":70}	
for student in student_DB:
	if student_DB["age"]==20:
		print(student_DB["age"])
		break

		'''

posts = [
    {
        "post_id": 1,
        "post": "From one small room to a home for Africa’s builders. 🚀 #BlockfuseAt1 #Web3Africa"
    },
    {
        "post_id": 2,
        "post": "Step inside our new facility — classrooms, engineering lab, media room, and space for 200+ students. #InnovationLivesHere"
    },
    {
        "post_id": 3,
        "post": "Ideas to Impact: Our students are shipping dApps, smart contracts, and open-source projects that solve real problems. #Web3Africa"
    },
    {
        "post_id": 4,
        "post": "The heartbeat of Blockfuse Labs is our people — students, mentors, engineers, and the community powering the journey. #CommunityOfBuilders"
    },
    {
        "post_id": 5,
        "post": "Year One built the foundation. Year Two will be the launch. Join us in shaping Africa’s Web3 future. #BlockfuseAt1 #InnovationLivesHere"
    }
]
user_id = int(input("Enter post: "))
user_post = None
for post in posts:
	if post["id"]==user_id:
		user_id = post
		break
if user_id !=None
	print(user_id)
else:
	print("No post with such ID")


