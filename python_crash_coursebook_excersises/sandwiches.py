#arbitrary argument function calls

#def sandwiches(*items):
#    print(items)

#sandwiches('ham', 'cheese', 'lettuce')
#sandwiches('sausage', 'egg')
#sandwiches('halloumi', 'tzaksiki')

#arbitrary keyword arguments
#def build_profile(first, last, **user_info):
#    user_info['first_name'] = first
#    user_info['last_name'] = last
#    return user_info

#user_profile = build_profile('owen', 'wykes', location="atherstone", profession="student", course="CS")
#print(user_profile)

def make_car(manufacterer, model, **other_details):
    other_details['Manufacturer'] = manufacterer
    other_details['model'] = model
    return other_details


car = make_car('honda', 'civic', color="blue", decat=True)

print(car)