"""
The program will print form letters asking for votes in the upcoming election
(the number of letters depends upon user input)
If user provides no input data, she is going to be presented with a goodbye message
When user is asked for resources the only restrictions are for those to be > 0 and < 10 chars
The program does NOT treat integers as invalid input, because the user might be talking in a secret language using code
names
If the user input does not satisfy the validation of input an error is going to be raised
"""


# Get resource after performing validations
# The reason for not baking in the min and max sizes
# Is because we want to keep it an option for individual
# Resource to specify the desired size limitations
def get_resource(resource_name, min_size, max_size):
    resource = ask_for_resource(resource_name)
    if is_resource_valid(resource, min_size, max_size):
        return resource
    else:
        raise ValueError("Length of input should be between {} and {}".format(min_size, max_size))


# Ask user for a resource
def ask_for_resource(resource_name):
    resource = input("Who is the {}? ".format(resource_name))
    return resource


# Check if input is valid
def is_resource_valid(text, min_size, max_size):
    text_size = len(text)

    if text_size > min_size or text_size < max_size:
        return True
    return False


# Define minimum number of chars to be allowed for a resource
MIN_RESOURCE_INPUT_SIZE = 0
# Define maximum number of chars to be allowed for a resource
MAX_RESOURCE_INPUT_SIZE = 10
# Define message that is going to be asked every time before new letter is about to be composed
new_template_message = "Would you like to template a new message?(yY/nN) "
# Define base message that is going to be build after data injection
base_message = "\nDear {0},\nI would like you to vote for {1}\n" + \
               "because I think {1} is best for\nthis country.\n" + \
               "Sincerely,\n{2}"

# The final resources list
resources = []

# Event loop starts
while True:
    # Ask user if she is interested in adding more messages
    add_new_message_event = input(new_template_message).capitalize()

    # Break the event loop if no more messages desired
    # or if user input does not make sense
    if add_new_message_event != 'Y':
        break

    # Ask for addressee
    addressee = get_resource('addressee', MIN_RESOURCE_INPUT_SIZE, MAX_RESOURCE_INPUT_SIZE)
    # Ask for candidate
    candidate = get_resource('candidate', MIN_RESOURCE_INPUT_SIZE, MAX_RESOURCE_INPUT_SIZE)
    # Ask for sender
    sender = get_resource('sender', MIN_RESOURCE_INPUT_SIZE, MAX_RESOURCE_INPUT_SIZE)
    # push the resulting tuple to messages specifics list
    resources.append((addressee, candidate, sender))

# Make sure user is presented with a nice goodbye message if no data have been provided
if not resources:
    print("\nGoodbye for now, seems like you are not in the mood to write any letters today")

# Loop over the data and display as a complete message
for spec in resources:
    print(base_message.format(*spec))
