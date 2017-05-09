#!/usr/bin/env python3
import characters
import util
import story
from story import basic_campaign



def introduction():
    print("Welcome to Geirrod's Castle")
    print("Please choose your class")


def pester(choices):
    print("Valid choices are %s" % ", ".join((choices)))


def event_loop(choices):
    pester(choices)
    choice = util.Prompt()
    while choice not in choices:
        pester(choices)
        choice = util.Prompt()


def main():
    introduction()
    # probably should name space that better, but it does show you the
    # module / namespace hierarchy in python
    playable = characters.classes.show_playable_characters()

    event_loop(playable)
    campaign = story.Campaign(basic_campaign.scenario)

    player = characters.New()
    campaign.Chapter("preface")


if __name__ == '__main__':
    main()
