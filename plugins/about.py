class AboutSession:

    about = "Amber is a bot framework built around the Discord bot APIs.\n\n\
You can view the source code, or even build your own bot at\
https://github.com/joshdabosh/amber.\n\nThanks!"

    def __init__(self, client, config):
        self.client = client
        self.config = config
	
    
    async def respond(self, message):
        await self.client.send(self.about, message.channel)

def load(client, config):
    return AboutSession(client, config)
