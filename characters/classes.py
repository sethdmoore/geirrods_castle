# all classes
from . import stats

# crush that namespace
base_stats = stats.base_stats

character_classes = {
        "warrior": {
            "str": base_stats["str"] * 1.2,
            "dex": base_stats["agi"] * 0.9,
            "spd": base_stats["spd"] * 0.8,
            "int": base_stats["spd"] * 1.2,
            "dur": base_stats["dur"] * 1.2,
            "playable": True
            },
        "monk": {
            "str": base_stats["str"] * 1.1,
            "dex": base_stats["agi"] * 1.1,
            "spd": base_stats["spd"] * 1.1,
            "int": base_stats["spd"] * 1.2,
            "dur": base_stats["dur"] * 0.7,
            "playable": True
        },
        "thief": {
            "str": base_stats["str"] * 0.8,
            "dex": base_stats["agi"] * 2.0,
            "spd": base_stats["spd"] * 1.1,
            "int": base_stats["spd"] * 0.5,
            "dur": base_stats["dur"] * 0.8,
            "playable": True
            },
        "archer": {
            "str": base_stats["str"] * 1.0,
            "dex": base_stats["agi"] * 1.2,
            "spd": base_stats["spd"] * 1.2,
            "int": base_stats["spd"] * 1.1,
            "dur": base_stats["dur"] * 0.6,
            "playable": True
            },
        "grunt": {
            "str": base_stats["str"] * 0.3,
            "dex": base_stats["agi"] * 0.2,
            "spd": base_stats["spd"] * 0.1,
            "int": base_stats["spd"] * 0.1,
            "dur": base_stats["dur"] * 0.6,
            "playable": False
            }
}


class Pawn(object):
    def __init__(self, char_class, name, is_dead=False):
        self.char_class = character_classes[char_class]
        self.name = name
        self.is_dead = is_dead

    def foo(self):
        pass


def show_playable_characters():
    pcs = [c for c in character_classes.keys() if character_classes[c]["playable"]]
    return pcs
