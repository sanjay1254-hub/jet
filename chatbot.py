print("Welcome to the Chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: You said:", user_input)