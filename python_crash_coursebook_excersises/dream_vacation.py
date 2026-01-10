responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit anywhere in the world where would you go? ")

    responses[name] = response

    repeat = input("Is there another person to ask? yes/no ")
    if repeat == 'no':
        polling_active = False  

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}")

