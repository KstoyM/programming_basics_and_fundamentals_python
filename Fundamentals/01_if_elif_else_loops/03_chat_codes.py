messages_sent = int(input())
secret_message = ''

for message_cnt in range(messages_sent):
    message_text = int(input())
    if message_text == 88:
        secret_message = 'Hello'
    elif message_text == 86:
        secret_message = 'How are you?'
    elif message_text < 88:
        secret_message = 'GREAT!'
    else:
        secret_message = 'Bye.'
    print(f'{secret_message}')