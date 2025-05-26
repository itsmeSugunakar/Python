# chatbot.py (logic only - optional)
def get_bot_response(user_message_lower):
    try:
        user_message_lower = user_message_lower.lower().strip()
        if "hello" in user_message_lower or "hi" in user_message_lower:
            response = "Hello! How can I help you today?"
        elif "data" in user_message_lower:
            response = "Are you interested in data analytics, data engineering, or data governance?"
        elif "bye" in user_message_lower or "goodbye" in user_message_lower:
            response = "Goodbye! Have a great day!"
        elif "help" in user_message_lower:
            response = "Sure, I can help! Ask me about our data science services or say 'menu' for options."
        elif "menu" in user_message_lower:
            response = "Options: Consulting, Analytics, Cloud Solutions, Governance. What would you like to know more about?"
        else:
            response = "I'm sorry, I didn't understand that. Can you please rephrase or ask about our services?"
        return response
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"
# chatbot.py (logic only - optional)