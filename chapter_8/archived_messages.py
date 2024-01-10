# 8-11. Archived Messages: pg 146
# MODIFIES 8-10. Sending Messages: pg 146

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
    
    print("Empty texts list: ", texts)
    print("Sent messages: \n", sent_messages)

# This time pass in a copy of the original texts list
send_messages(texts[:], sent_messages)
print("Original Texts: ", texts)
