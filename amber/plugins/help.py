import discord

class HelpSession:

    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.buildUsage()

        
    def buildUsage(self):
        self.usage = discord.Embed(title=("Commands that Amber understands:".format(self.client.conf['PREFIX'])), color=int(self.client.conf["COLOR"], 16))
        for command in self.config['commands']:
            self.usage.add_field(name=command, value=self.config['commands'][command], inline=False)


    async def respond(self, message):
        await self.client.embed(self.usage, message.channel)

def load(amber, config):
    return HelpSession(amber, config)
