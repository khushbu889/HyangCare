import torch

print("🌸 Welcome to HyangCare")
print("Type 'bye' to exit\n")

responses = {
    "sad": "I'm really sorry you're feeling this way. You're not alone 💙",
    "stress": "That sounds overwhelming. Take a deep breath — one step at a time 🌱",
    "lonely": "Feeling lonely can be really hard. I'm here with you 🤍",
    "happy": "That's lovely to hear! Keep smiling 😊"
}

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("HyangCare: Take care 💐 I'm always here.")
        break

    reply = "Thank you for sharing. I'm listening."

    for key in responses:
        if key in user_input.lower():
            reply = responses[key]
            break

    print("HyangCare:", reply)