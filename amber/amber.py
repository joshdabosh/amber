import discord
import json
import logging
import importlib
import os

from command import Command

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

class Amber:
    def __init__(self):
        self.client = discord.Client()

        self.buildConf()
        self.buildCommands()
        

    def buildConf(self):
        self.conf = json.loads(open("config.json").read())
        

    def buildCommands(self):
        self.commands = dict()

        files = self.conf["plugins"]
        for name in files:
            path = os.path.join(os.getcwd(), files[name]["path"])
            
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            self.commands[name] = module.load(self, files[name])

            log.info("Added plugin '%s' to modules list", name)


    def start(self):
        @self.client.event
        async def on_ready():
            log.info("Logged in successfully!")

        @self.client.event
        async def on_message(message):

            log.info("Message received from %s: %s", message.author, message.content.strip())

            if message.author == self.client.user:
                return

            c = message.content.strip().split()

            if len(c) >= 2:
                if c[0] == self.conf["PREFIX"].strip():
                    if c[1] in self.commands.keys():
                        if callable(getattr(self.commands[c[1]], "respond", None)):
                            await self.commands[c[1]].respond(message)
                            log.info("Fired command '%s'", str(self.commands[c[1]]))
                        else:
                            log.info("Command '%s' is not callable", c[1])
                    else:
                        log.info("No such command '%s'", c[1])

                else:
                    return

            else:
                return
            
        self.client.run(self.conf["TOKEN"])


    async def send(self, message, channel):
        await channel.send(message)
        

    async def embed(self, embed, channel):
        await channel.send(embed=embed)


def main():
    amber = Amber()
    amber.start()


if __name__ == "__main__":
    main()
