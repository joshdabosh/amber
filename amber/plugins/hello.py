class HelloSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config


    async def respond(self, message):
        await self.client.send("Hello to you too~!", message.channel)

        return

def load(client, config):
    return HelloSession(client, config)
