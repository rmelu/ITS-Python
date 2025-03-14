def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    for message in messages[:]:
        print(f"invio del messaggio: {message}")
        sent_messages.append(message)
        messages.remove(message)

text_messages = [
    "ciao, come stai?",
    "ci vediamo domani?",
    "ricordati di studiare!",
    "buona giornata."
]
sent_messages = []
send_messages(text_messages, sent_messages)

print("\nLista dei messaggi originali: ")
print(text_messages)

print("\nLista dei messaggi inviati: ")
print(sent_messages)
