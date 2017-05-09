# the default story

preface = {
    "scenario": [
        "    You awaken inside of something cool, damp, and dark. Your eyes are too ",
        "tired to focus. You're unsure of your surroundings. You see splotches of ",
        "light amidst vast darkness. Something tight grips your arms and legs."
    ],
    "valid_choices": {
        "struggle": ["struggle"],
        "cry": ["cry", "call", "yell", "scream"],
        "look": ["observe", "look", "describe"]
    },
    "lethal_choices": {
        "cry": [
            "    You hear some thumping sounds in the distance. It sounds like something ",
            "large is heading your way! You panic, attempting to struggle. You notice",
            " something glinting in what you assume is the pale moonlight, but...",
            "It is too late. Something large and unwieldy begins lumbering nearer",
            " and nearer! It must be at least 9 feet tall! It slows its pace and kneels",
            "right in front of you; its ugly face twisting in to an approximation of a smile.",
            "    \"Human no stay quiet,\" it says, in its dumb and childlike way.",
            "\"I make human quiet,\" it yells. You see the creature move with unbelievable",
            " swiftness. A club-like object is raised and then swung towards your head before",
            " you even realize it. Everything goes black.",
            "", "",
            "You are dead"
            ]
    }
}

scenario = {
    "preface": preface
}

