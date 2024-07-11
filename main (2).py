import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing fine, how about you?",]
    ],
    [
        r"(.*) (hungry|tired|sleepy)",
        ["I'm sorry to hear that. Have you tried taking a break?",]
    ],
    [
        r"(.*) weather (.*)",
        ["You can check the weather on a weather website.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual assistant. I don't have a physical location.",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!", "It was nice talking to you. Goodbye!"]
    ],
]

# Create a Chatbot with NLTK
def chatbot():
    print("Hi, I'm Chatbot! How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            response = random.choice(pairs)[-1][0]
            print(f"Chatbot: {response}")
            break
        else:
            response = chat.respond(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
