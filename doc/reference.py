#!/usr/bin/env python3
# this was a script I wrote as an example for someone,
# but I'm keeping it as a reference.

# the token used to show player input
TOKEN = "> "

# for the intro
INITIAL_CHOICES = ["look", "move"]


# base stats for all {,N}PCs
BASE_STATS = {
            "str": 10,
            "agi": 10,
            "spd": 4,
            "int": 2,
            "dur": 8
            }


# all classes
CLASSES = {
        "warrior": {
            "str": BASE_STATS["str"] * 1.2,
            "dex": BASE_STATS["agi"] * 0.9,
            "spd": BASE_STATS["spd"] * 0.8,
            "int": BASE_STATS["spd"] * 1.2,
            "dur": BASE_STATS["dur"] * 1.2,
            "playable": True
            },
        "monk": {
            "str": BASE_STATS["str"] * 1.1,
            "dex": BASE_STATS["agi"] * 1.1,
            "spd": BASE_STATS["spd"] * 1.1,
            "int": BASE_STATS["spd"] * 1.2,
            "dur": BASE_STATS["dur"] * 0.7,
            "playable": True
        },
        "thief": {
            "str": BASE_STATS["str"] * 0.8,
            "dex": BASE_STATS["agi"] * 2.0,
            "spd": BASE_STATS["spd"] * 1.1,
            "int": BASE_STATS["spd"] * 0.5,
            "dur": BASE_STATS["dur"] * 0.8,
            "playable": True
            },
        "archer": {
            "str": BASE_STATS["str"] * 1.0,
            "dex": BASE_STATS["agi"] * 1.2,
            "spd": BASE_STATS["spd"] * 1.2,
            "int": BASE_STATS["spd"] * 1.1,
            "dur": BASE_STATS["dur"] * 0.6,
            "playable": True
            },
        "grunt": {
            "str": BASE_STATS["str"] * 0.3,
            "dex": BASE_STATS["agi"] * 0.2,
            "spd": BASE_STATS["spd"] * 0.1,
            "int": BASE_STATS["spd"] * 0.1,
            "dur": BASE_STATS["dur"] * 0.6,
            "playable": False
            }
}


class Pawn(object):
    def __init__(self, char_class, name, is_dead=False):
        self.char_class = CLASSES[char_class]
        self.name = name
        self.is_dead = is_dead


def show_playable_characters():
    pcs = [c for c in CLASSES.keys() if CLASSES[c]["playable"]]
    return pcs


def prompt():
    action = input(TOKEN)
    return action


def playable():
    pcs = [c for c in CLASSES.keys() if CLASSES[c]["playable"]]
    return pcs


def preface(choices):
    print("Choose the path that describes you best.")
    print_choices(choices)
    choice = prompt()

    while choice not in choices:
        print_choices(choices)
        choice = prompt()

    return choice

def print_choices(choices):
    print("Your choices are:")
    print("%s" % ", ".join((choices)))


def intro(choices):
    print(
"""You awaken inside of something cool, damp, and dark. Your eyes are too 
tired to focus. You're unsure of your surroundings. You see splotches of 
light amidst vast darkness. Something tight grips your arms and legs.
""")
    print_choices(choices)
    action = prompt()
    while action not in choices:
        print_choices(choices)
        action = prompt()
    if "look" in action:
        print(
"""You manage to focus your eyes and see naught but brick around you. You are 
surprised when you look at your wrists and notice shackels on them. Your 
ankles suffer the same fate. You despair at your misfortune."""
        )


def parse_input(choices):
    choice = prompt()
    while choice not in choices:
        print_choices(choices)
        choice = prompt()


def main():
    playable_classes = playable()

    char_class = preface(playable_classes)

    player = Pawn(char_class)

    initial_choices = INITIAL_CHOICES
    intro(initial_choices)


if __name__ == '__main__':
    main()
