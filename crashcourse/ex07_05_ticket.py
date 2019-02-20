prompt = "How old are you?"
prompt += "\nPlease enter 'quit' to quit. "

message = input(prompt)
while message != 'quit':
    message = int(message)
    if message < 3:
        print("Hi. You do not have to pay.")
    elif message <= 12:
        print("Hi. The ticket will be $10.")
    else:
        print("Hi. The ticket will be $15.")
    message = input(prompt)


