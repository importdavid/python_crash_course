# 8-10. Sending Messages: pg 146
# MODIFIES 8-9. Messages: pg 146

texts = [
    'hey',
    'sup?',
    'nm, u?',
]

sent_messages = []

def send_messages(texts, sent_messages):
    while texts:
        text = texts.pop()
        print(text)
        sent_messages.append(text)
    
    print("Sent messages: \n", sent_messages)

send_messages(texts, sent_messages)
