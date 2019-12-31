import asyncio, random

class EightBallSession:

    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def respond(self, message):
        await self.client.send(random.choice(self.answers), message.channel)


def load(client, config):
    return EightBallSession(client, config)
