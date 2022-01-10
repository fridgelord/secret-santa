import random

players = {
    "Marcin": {
        "email": "temp@gmail.com",
        "unpair": [],
    },
    "Hania": {
        "email": "hania@gmail.com",
        "unpair": ["Asia"],
    },
    "Asia": {
        "email": "tempasia@gmail.com",
        "unpair": [],
    },
}

def save_data():
    pass


def ranomize_pairs(players):
    names = list(players.keys())
    counterparts = names.copy()
    random.shuffle(counterparts)
    pairs = tuple(zip(names, counterparts))
    return pairs

def pairs_incompatibile(players, pairs):
    for pair in pairs:
        if (pair[0] == pair[1]) or (pair[1] in players[pair[0]]["unpair"]):
            return True
    return False


def select_pairs(players):
    pairs = ranomize_pairs(players)
    while pairs_incompatibile(players, pairs):
        pairs = ranomize_pairs(players)
    return pairs


print(select_pairs(players))

