#Basic Rule-Based Chatbot
print("Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input=input("You: ").lower()
    
    if user_input == "hello":
        print("Bot: Hi!")
    elif user_input == "how are you":
        print("Bot: I am fine, thank you!")
    elif user_input == "what is your name":
        print("Bot: I am a simple chatbot.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.....")
        break
    else:
        print("Bot: Sorry I don't understand")