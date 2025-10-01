def chatbot():
    responses = {
        "hello": "Hi!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks! How about you?",
        "what's up": "All good here!",
        "bye": "Goodbye! Have a nice day!",
        "thanks": "You're welcome!"
    }

    print("=== Simple Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "":
            print("Bot: Please say something.")
            continue

        if user_input in responses:
            print(f"Bot: {responses[user_input]}")
        else:
            print("Bot: Sorry, I don't understand that.")

        if user_input == "bye":
            break


if __name__ == "__main__":
    chatbot()
