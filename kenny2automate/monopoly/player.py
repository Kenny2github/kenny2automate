from enum import IntFlag

class PlayerState(IntFlag):
    NOTHING = 0b0000
    JAILED1 = 0b0001
    JAILED2 = 0b0010
    JAILED3 = 0b0100
    HAS_GOJ = 0b1000
    IN_JAIL = 0b0111

class Player:
    def __init__(
        self, name, id, token,
        owned=None, on=0, worth=1500,
        state=PlayerState.NOTHING
    ):
        self.name = name
        self.id = id
        self.token = token
        self.owned = owned or set()
        self.on = on
        self.worth = worth
        self.state = state

    name: str #player name
    id: int #player ID
    token: int #token number

    def __repr__(self):
        return self.name

    #dynamic
    owned: set = set() #set of int spaces
    on: int = 0 #int space that the player is on
    worth: int = 1500 #net worth
    state: PlayerState = PlayerState.NOTHING
