from random import choices

my_ticket = [34, 5 , 8, 'Q']
lottery = [34, 22, 'T', 5, 8, 'W', 12, 54, 'Q', 21, 9, 'H', 2, 4, 'S']
loop_count = 0

while True:
    results = choices(lottery, k=4)
    if set(results) == set(my_ticket):
        print(f"The lottery ran {loop_count} times before you won" )
        break
    else: 
        loop_count += 1

print(f"If any tickets match {results} they win a prize!")
