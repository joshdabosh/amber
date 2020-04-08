# Amber
<img src="amber.JPG" width="100" align="right">

Amber is a framework for making Discord bots. It contains only a few sample plugins, but custom plugins can be easily added and sculpted to one's imagination. Plugins are functions that are called whenever a user on Discord communicates with the bot with a prefix. By default, the prefix is `/amber`. For example, the `hello` plugin greets the user when they send `/amber hello`.

Amber takes its inspiration from [pearl](https://github.com/defund/pearl), and is built on [discord.py](https://github.com/Rapptz/discord.py).

Amber is meant for you to develop and experiment with. :)

## Requirements

Amber requires a Discord bot account. You can find out how to make one and invite it to servers [here](https://discordpy.readthedocs.io/en/latest/discord.html). Save the token you copy from step 7, and feel free to add it to as many servers as you like.

Clone / download the repository.

After doing so, run the file `customize.py` and select the first option.

It will end up prompting you for:
* A token - The token you copied from step 7 of the bot creation guide.
* A prefix - What you want the bot to respond to. Could be `/` or `/amber `(note the space) for example.
* A color - What color you want the bot to be themed, in hexadecimal. For example, a color could be `FCC5B1`. Capitalization doesn't matter in this case, so it could also be `fcc5b1`

After filling that out, the bot should be ready to run. Make sure to exit `customize.py` with the menu option so that it knows to save the new config.

## Running
To give start, first cd into the `amber/` directory and install dependencies:
`pip3 install -r requirements.txt`

Then, simply run `python3 amber.py`.

In any server with Amber, try sending `/amber help`. Amber should respond with a set of available commands.

Alternatively, you can build and run the provided Dockerfile.


## Customization
Generally speaking, `amber.py` should not be modified as it only handles the distribution of plugin tasks. Instead, customize Amber by making new plugins inside the `amber/plugins` directory and running `customize.py` to add them.

## Onward
This is still an ongoing project, so feel free to reach out to me with any questions or suggestions (hey that kind of rhymes!)
