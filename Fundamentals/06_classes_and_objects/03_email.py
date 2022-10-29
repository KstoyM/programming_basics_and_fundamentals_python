class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_lst = []

while True:
    command = input()

    if command == "Stop":
        break

    sender1, receiver1, content1 = command.split(" ")

    email = Email(sender1, receiver1, content1)
    email_lst.append(email)

sent_emails = [int(x) for x in input().split(", ")]

for x in sent_emails:
    email_lst[x].send()

for email in email_lst:
    print(email.get_info())
