import time

#intial exchange
print("Hi, My name is Chatbot")

#name input
user_name = input("What is your name? ")
print(f"Nice to meet you {user_name}")

#age input and chatbot age storage
chatbot_age = 32
user_age = int(input("How old are you? "))

#age difference sum
age_difference = chatbot_age - user_age

#age difference working
if (age_difference > 0):
    print(f"I'm {age_difference} years older than you")
elif (age_difference < 0):
    print(f"I'm {-age_difference} years younger than you")
else:
    print("We're the same age!")

#short wait
time.sleep(2)

#goodbye statement  
print(f"It's nice chatting to you {user_name}. Hope to see you around. Have a nice day")

