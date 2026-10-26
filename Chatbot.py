
# Task 1: Rule-Based Chatbot

def chatbot(user_input):
    # Convert input to lowercase for easier matching
    message = user_input.lower().strip()

    # Respond to greetings
    if message in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    # Respond to common questions
    elif "your name" in message:
        return "I am a simple Python chatbot."

    elif "how are you" in message:
        return "I am doing well! Thank you."

    elif "help" in message:
        return "I can answer greetings and simple questions."

    elif "bye" in message:
        return "Goodbye! Have a nice day!"

    # Fallback for unknown input
    else:
        return "Sorry, I don't understand that yet."


# Run the chatbot
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Chatbot:", response)

    if user.lower().strip() == "bye":
        break
