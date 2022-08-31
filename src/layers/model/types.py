from enum import Enum
from typing import TypedDict, Optional, Literal


class GameStages(str, Enum):
    GAME_STARTING_IS_AWAITED = 'gameStartingIsAwaited'
    BET_IS_AWAITED = 'betIsAwaited'
    CARD_TAKING_IS_AWAITED = 'cardTakingIsAwaited'
    FINISHED = 'finished'


class PlayerNames(str, Enum):
    SKYNET = 'skynet'
    PLAYER = 'player'


class Player(TypedDict):
    money: int
    deck: list[int]
    score: int


class Game(TypedDict):
    stage: Literal[GameStages.GAME_STARTING_IS_AWAITED,
                   GameStages.BET_IS_AWAITED, GameStages.CARD_TAKING_IS_AWAITED, GameStages.FINISHED]
    deck: list[int]
    bank: int
    winner: Optional[PlayerNames]
    skynet: Player
    player: Player
