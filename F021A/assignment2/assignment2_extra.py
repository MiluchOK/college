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
        raise ValueError("Length of input should be between {} and {}.".format(min_size, max_size))


# Ask user for a resource
def ask_for_resource(resource_name):
    resource = input("Who is the {}? ".format(resource_name))
    return sanitize(resource)


# Sanitize the text
def sanitize(text):
    return text.strip()


# Check if input is valid
def is_resource_valid(text, min_size, max_size):
    text_size = len(text)

    if min_size < text_size < max_size:
        return True
    return False


# Ask for a resource with the MIX MAX input restrictions and recursively retry on input error
def safe_ask(resource_name, min_size, max_size):
    try:
        return get_resource(resource_name, min_size, max_size)
    except ValueError as e:
        print(e, " Try again.")
        return safe_ask(resource_name, min_size, max_size)


# Define minimum number of chars to be allowed for a resource
MIN_RESOURCE_INPUT_SIZE = 0
# Define maximum number of chars to be allowed for a resource
MAX_RESOURCE_INPUT_SIZE = 50
# Define message that is going to be asked every time before new letter is about to be composed
new_template_message = "\nWould you like to template a new message?(yY/nN) "
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
    addressee = safe_ask('addressee', MIN_RESOURCE_INPUT_SIZE, MAX_RESOURCE_INPUT_SIZE)
    # Ask for candidate
    candidate = safe_ask('candidate', MIN_RESOURCE_INPUT_SIZE, MAX_RESOURCE_INPUT_SIZE)
    # Ask for sender
    sender = safe_ask('sender', MIN_RESOURCE_INPUT_SIZE, MAX_RESOURCE_INPUT_SIZE)
    # push the resulting tuple to messages specifics list
    resources.append((addressee, candidate, sender))

# Make sure user is presented with a nice goodbye message if no data have been provided
if not resources:
    print("\nGoodbye for now, seems like you are not in the mood to write any letters today")

# Loop over the data and display as a complete message
for spec in resources:
    print(base_message.format(*spec))


"""
Would you like to template a new message?(yY/nN) y
Who is the addressee? Hildegard
Who is the candidate? Hillary Clinton
Who is the sender? Brunhilda

Would you like to template a new message?(yY/nN) y
Who is the addressee? Cheech
Who is the candidate? Donald Trump
Who is the sender? Chong

Would you like to template a new message?(yY/nN) y
Who is the addressee? Moe
Who is the candidate? Bernie Sanders
Who is the sender? Jack

Would you like to template a new message?(yY/nN) n

Dear Hildegard,
I would like you to vote for Hillary Clinton
because I think Hillary Clinton is best for
this country.
Sincerely,
Brunhilda

Dear Cheech,
I would like you to vote for Donald Trump
because I think Donald Trump is best for
this country.
Sincerely,
Chong

Dear Moe,
I would like you to vote for Bernie Sanders
because I think Bernie Sanders is best for
this country.
Sincerely,
Jack
"""