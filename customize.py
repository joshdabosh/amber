import json
import os

def write(fname, cf):
    with open(fname, "w") as f:
        f.write(json.dumps(cf, indent=4, sort_keys=True))


def check(act, g):
    while 1:
        try:
            act = int(act)
            assert act in g
            break

        except ValueError:
            act = input("Non-integer input, try again: ")

        except AssertionError:
            act = input("Bad number, try again: ")

    return act


cmds = {2:"token",
        3:"prefix",
        4:"color"}


config = json.load(open("amber/config.json"))

write("amber/config.json.bak", config)


print("""Welcome to the Amber config.json customizer.\n
Your options are:\n
\t1. Configure All
\t2. Change token
\t3. Change prefix
\t4. Change color (must be hexadecimal)
\t5. Modify command
\t6. Exit\n""")

act = input(": ").strip()


while 1:
    act = check(act, range(1,7))

    if act == 1:
        for i in range(2, 5):
            config[cmds[i].upper()] = input("New " + cmds[i] + ": ").lstrip("0x").lstrip("#").strip()

    elif 2 <= act and act <= 4:
        config[cmds[act].upper()] = input("New " + cmds[act] + ": ").lstrip("0x").lstrip("#").strip()

    elif act == 5:
        c = input("\t1. Add command\n\t2. Remove command\n:")
        c = check(c, range(1,3))

        if c == 1:
            name = input("Command name: ").strip()
            d = input("Path from plugins directory: ").strip()
            desc = input("Brief command descrition: ").strip()

            config["plugins"][name] = {"path":os.path.join("plugins", d)}
            config["help"]["commands"][name] = desc

            print("Added command " + name)

        else:
            name = input("Command name: ").strip()
            
            try:
                del config["plugins"][name]
                print("Successfully deleted command " + name)

            except KeyError:
                print("No such command " + name)
        
    elif act == 6:
        break

    print()

    act = input("Next action: ").strip()


write("amber/config.json", config)





