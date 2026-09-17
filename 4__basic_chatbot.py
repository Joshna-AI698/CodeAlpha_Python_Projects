def chatbot():
    print("Hello1 I am a basic chatbot.")
    print("You cam say hello,ask how I am,or say bye.")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ["hello", "hi", "hey"]:
            print("Hi! How can I help you?")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input in ["what is your name", "your name"]:
            print("Bot: I'm a basic python chatbot.")
        elif user_input == "help":
            print("Bot: You can say hello,ask how I am, or say bye.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye!")
        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
