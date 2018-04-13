"""
The program will print form letters asking for votes in the upcoming election
(the number of letters depends upon user input)
"""

new_template_message = "Would you like to template a new message? "
resource_question = "Who is the {}? "

base_message = "\nDear {0},\nI would like you to vote for {1}\n" + \
               "because I think {1} is best for\nthis country.\n" + \
               "Sincerely,\n{2}"

messages_specifics = []

# Event loop starts
while True:
    # Ask user if she is interested in adding more messages
    add_new_message_event = input(new_template_message)

    # Break the event loop if no more messages desired
    if add_new_message_event.capitalize() == 'N':
        break

    # Ask for addressee
    addressee = input(resource_question.format('addressee'))
    # Ask for candidate
    candidate = input(resource_question.format('candidate'))
    # Ask for sender
    sender = input(resource_question.format('sender'))
    # push the resulting tuple to messages specifics list
    messages_specifics.append((addressee, candidate, sender))

for spec in messages_specifics:
    print(base_message.format(*spec))
