import discord
import json
import logging
import importlib
import os
import sys

from command import Command

if len(sys.argv) > 1:
    if sys.argv[2] in ["-v", "--verbose"]:
        logging.basicConfig(format="%(levelname)s:%(module)s:%(message)s", level=logging.DEBUG)
else:
    logging.basicConfig(format="%(levelname)s:%(module)s:%(message)s", level=logging.INFO)


log = logging.getLogger(__name__)


class Amber:
    def __init__(self):
        self.client = discord.Client()

        self.buildConf()
        self.buildCommands()
        

    def buildConf(self):
        try:
            self.conf = json.loads(open("secret/config.json").read())
        except:
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

            if message.author == self.client.user:
                return

            log.debug("Message received from %s: %s", message.author, message.content.strip())

            c = message.content.strip()

            if c.startswith(self.conf["PREFIX"]):
                c = message.content.replace(self.conf["PREFIX"], "").strip().split()

                if c[0] in self.commands.keys():
                    if callable(getattr(self.commands[c[0]], "respond", None)):
                        await self.commands[c[0]].respond(message)
                        log.debug("Fired command '%s'", str(self.commands[c[0]]))
                    else:
                        log.warning("Command '%s' is not callable (no respond method)", c[0])
                else:
                    log.warning("No such command '%s'", c[0])
                    
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
