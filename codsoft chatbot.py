def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define some predefined rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main function to run the chatbot
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
