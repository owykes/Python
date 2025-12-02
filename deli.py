sandwich_orders = ['blt' , 'club', 'pastrami','tuna', 'pastrami','egg', 'ham', 'cheese', 'pastrami', ]
finished_sandwiches = []

print("Them deli has ran out of pastrami sandwiches")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()} sandwich")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwhiches were made:")
for sandwhich in finished_sandwiches:
    print(f"\t{sandwhich.title()}")
    