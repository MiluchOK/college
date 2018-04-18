"""
The program will print three form letters asking for votes in the upcoming election
"""

base_message = "Dear {0},\nI would like you to vote for {1}\n" + \
               "because I think {1} is best for\nthis country.\n" + \
               "Sincerely,\n{2}"

messages_specifics = [
    ('Hildegard', 'Hillary Clinton', 'Brunhilda'),
    ('Cheech', 'Donald Trump', 'Chong'),
    ('Moe', 'Bernie Sanders', 'Jack')
]

for spec in messages_specifics:
    print(base_message.format(*spec) + "\n")