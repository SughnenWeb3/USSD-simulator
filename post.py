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
user_post_id = int(input("Enter post ID: "))
for post in posts:
	if post["post_id"]==user_post_id:
		print(post['post'])
		break
else:
	print("Post does not exist")


'''
'''
import random 
count = 5
secret_num = random.randint(1,10)  #10
i = 1

while i<=count:
	user_guess = int(input("Enter lucky number: "))
	if user_guess > secret_num:
		print("Guess is greater than secret number")
	elif user_guess < secret_num:
		print("Guess is less than secret number")
	else:
		print("Correct")
		break
'''
	
'''
counter = 10
while counter>=1:
	print(counter)
	counter-=1
'''
'''
percent = 100
phone_percent = 0

while phone_percent <= 100:
	charge = int(input("Percent to add: "))
	phone_percent += charge
	time.sleep(5)
	print(f"Charging: {phone_percent}")
'''
'''
count = 1
while count <=100:
	if count % 2 !=0:
		print(count)
	count+=1
'''

students = {
"John":60,
"Mimi":50,
"Sarah":30
	}
student_keys=list(students.keys())
student_len = len(student_keys)
counter = 0
while counter < student_len:
	print(student[counter])
	counter+=1

