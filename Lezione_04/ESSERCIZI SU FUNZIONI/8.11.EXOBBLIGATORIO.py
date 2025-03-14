def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
        sent_messages.append(message)
messages = ['ciao!', 'che si dice', 'a domani!']
sent_messages = []

send_messages(messages[:], sent_messages)

print("\nLista originale: messages")
print("\nLista dei messaggi inviati:", sent_messages)
print()