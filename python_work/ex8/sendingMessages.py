def show_messages(messages):
    """split list of various msg and print each msg."""
    for msg in messages:
        print(msg + '.')

def send_messages(messages, sent_messages):
    """"""
    print('-----------------------')
    while messages: # True until msgs list is not empty.
        current_msg = messages.pop()
        print(f'Sending message: {current_msg}')
        sent_messages.append(current_msg)


msgs = ['I love you', 'Moon halo', "You're my special"]
sent_messages = []

show_messages(msgs)
send_messages(msgs, sent_messages)

print(f'\nmsgs list >> {msgs} \nsent_messages list >> {sent_messages}')
