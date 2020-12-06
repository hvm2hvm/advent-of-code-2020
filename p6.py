import functools

data = open("input/p6", "rb").read().decode()

anyone = (len(set(group) & set("abcdefghijklmnopqrstuvwxyz"))
          for group in data.split("\n\n"))

print(f"Anyone: {sum(anyone)}")

everyone = (len(functools.reduce(set.intersection,
                             map(set, group.split("\n")),
                             set("abcdefghijklmnopqrstuvwxyz"))
                )
            for group in data.split("\n\n"))

print(f"Everyone: {sum(everyone)}")
