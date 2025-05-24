# chatbot.py (logic only - optional)
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."