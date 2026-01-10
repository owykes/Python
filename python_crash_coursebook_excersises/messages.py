messages = ["You're the best", "Have a nice day", "Carry on"]
sent_messages = []

def show_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)



show_messages(messages[:])
print(messages)
print(sent_messages)