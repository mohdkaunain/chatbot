def simple_chatbot(user_input):

    user_input = user_input.lower()

   
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"


def main():
    print("Welcome to the Simple Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(simple_chatbot(user_input))
            break
        else:
            print("Bot:", simple_chatbot(user_input))

if __name__ == "__main__":
    main()
