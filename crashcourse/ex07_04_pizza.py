prompt = "Please enter a souce for pizza."
prompt += "\n(Enter 'quit' to finish.)"

message = input(prompt)
while message != 'quit':
    print("We will add "+ message + " into the pizza!")
    message = input(prompt)

