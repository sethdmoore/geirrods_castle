#!/usr/bin/env python3
import characters
import util
import story
from story import basic_campaign


def introduction(playable_characters):
    print("Welcome to Geirrod's Castle.")
    name = util.Get_Name()

    print("Please choose your class.")

    player_class = event_loop(playable_characters, confirm=True)
    return name, player_class


def event_loop(choices, confirm=False):
    # pester(choices)
    output = ", ".join(choices)
    choice = util.Prompt(text=output, confirm=confirm)

    while choice not in choices:
        # pester(choices)
        choice = util.Prompt(text=output, confirm=confirm)

    return choice


def main():
    # probably should name space that better, but it does show you the
    # module / namespace hierarchy in python
    playable = characters.classes.show_playable_characters()

    name, player_class = introduction(playable)


    player = characters.New(player_class, name)

    # in theory if you wanted to make your own campaign you would create
    # story/foo_campaign.py and add a scenario dictionary there.
    # Or you could be crazy awesome and make it read from some fancy JSON-spewing
    # API in the fluffy clouds somewhere.
    campaign = story.Campaign(basic_campaign.scenario)

    campaign.Chapter("preface")

    chocie = event_loop(campaign.choices)


if __name__ == '__main__':
    main()
