class Card:
    def __init__(self, name: str):
        self._name = name

    def name(self):
        return self._name


class Weapon(Card):
    # weapons
    W_CANDLESTICK = 'Candlestick'
    W_DAGGER = "Dagger"
    W_LEADPIPE = "Lead Pipe"
    W_REVOLVER = "revolver"
    W_ROPE = "Rope"
    W_WRENCH = "wrench"


class Room(Card):
    # rooms
    R_STUDY = 'The Study'
    R_KITCHEN = "Kitchen"
    R_BALLROOM = "Ballroom"
    R_CONSERVATORY = "Conservatory"
    R_BILLIARDROOM = "Billiard Room "
    R_LIBRARY = " Library"
    R_HALL = "Hall"
    R_LOUNGE = "Lounge"
    R_DININGROOM = "Dining Room"


class Suspect(Card):
    # suspects
    S_REVGREEN = 'Rev. Green'
    S_COLMUSTERD = "Colenal Musterd"
    S_PEACOCK = "Mrs.peacock"
    S_PROFPLUM = "Profeser Plum"
    S_MISSSCAERLET = "Miss Scarlet"


# a lot of code here

c = Weapon(Weapon.W_CANDLESTICK)
print(c.name())
d = Room(Room.R_BALLROOM)
print(d.name())
