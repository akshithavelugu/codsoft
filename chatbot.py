import re
def respond_to_user(user_input):
    user_input=user_input.lower().strip()
    if re.search(r"\b(hi|hello|hey)\b",user_input):
        return "Hello! How can I assist you today?"
    elif "what can you do" in user_input:
        return "I am like your friend,feel free to ask me anything"
    elif "how are you" in user_input:
        return "I am good, thank you! How about you?"
    elif "time" in user_input:
        from datetime import datetime
        return f"The time is {datetime.now().strftime('%H:%M:%S')}."
    elif re.search(r"\b(who created you|who made you)\b", user_input):
        return "I was created by a team of developers who love coding and AI."
    elif "joke" in user_input:
        return "Students and teachers are like software and hardware, they work best when they are compatible!"
    elif "love" in user_input:
        return "Love is like a software update, it makes everything better!"
    elif "weather" in user_input:
        return "I can't check the weather right now, but I hope it's nice where you are!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"   
print("Chatbot:How Can I help you?")
if __name__ == "__main__":
    while True:
        user_input=input("You:")
        if user_input.lower()=="bye":
            print("Chatbot:",respond_to_user(user_input))
            break
        else:
            print("Chatbot:", respond_to_user(user_input))
        