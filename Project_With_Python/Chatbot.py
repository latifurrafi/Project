import tkinter as tk
import random

# Predefined responses for the chatbot
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"],
    "how are you": ["I'm just a bot, but I'm doing well! How about you?", "I'm doing great, thank you!"],
    "your name": ["I'm your friendly chatbot!", "I don't have a name, but I'm here to assist you."],
    "bye": ["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"],
    "default": ["I'm not sure I understand. Can you try asking in a different way?", 
                "Sorry, I don't know how to respond to that.", 
                "Hmm, I'm not sure. Can you rephrase?"]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Function to handle sending a message
def send_message(event=None):  # Added 'event' parameter for binding
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_history.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)  # Clear the input field

    if user_input.lower() == "bye":
        response = random.choice(responses["bye"])
        chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        window.after(2000, window.quit)
        return

    response = get_response(user_input)
    chat_history.insert(tk.END, "Chatbot: " + response + "\n")

# Create the main `tkinter` window
window = tk.Tk()
window.title("Chatbot")
window.geometry("400x500")

# Chat history display
chat_history = tk.Text(window, bd=1, bg="light gray", height=20, width=50)
chat_history.config(state=tk.NORMAL)
chat_history.pack(pady=10)

# Input field
entry = tk.Entry(window, bd=1, bg="white", width=40)
entry.pack(pady=5)

# Bind the Enter key to the send_message function
entry.bind("<Return>", send_message)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Run the `tkinter` main loop
window.mainloop()
