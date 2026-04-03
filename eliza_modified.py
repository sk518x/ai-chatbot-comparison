import nltk
from nltk.chat.util import Chat, reflections

pairs = [

    (r"hello", [
        "Hello. How are you feeling today?"
    ]),

    (r"I feel (.*)", [
       "Do you often feel %1?"
           ]),

(r".*not (.*)", [
    "What happened to make you feel like this?"]),

    (r".*was (.*)", [
        "Did something happen on the way to your class?"
    ]),

(r".*late.*", [
        "Is there anything you can do to make yourself feel better?"
    ]),

    (r".*should.*", [ 
       "I see. And what does that tell you?"
     ]),

    (r"(.*)", [
        "Got something else you want us to talk about?"
    ])
]

chatbot = Chat(pairs, reflections)

if __name__ == "__main__":
    print("ELIZA Chatbot (Custom)")
    print("Type 'quit' to stop.\n")

    while True:
        user_input = input("> ")

        if user_input.lower() == "quit":
            print("Goodbye.")
            break

        response = chatbot.respond(user_input)
        print(response)
