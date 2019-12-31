class Command:
    def __init__(self, bot, name, regex=r''):
        self.bot = bot
        self.name = name
        self.re = re.compile(regex)
        

    def __repr__(self):
        return "<Command {} matching input {}>".format(name, regex)


    def getName(self):
        return self.name
    

    async def call(self, m):
        await self.func(m)
