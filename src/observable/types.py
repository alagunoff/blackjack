from typing import Literal, Callable

from layers.view import EventNames as ViewEventNames
from layers.model import EventNames as ModelEventNames


EventName = Literal[ViewEventNames.GAME_STARTED, ViewEventNames.BET_MADE,
                    ViewEventNames.CARD_TAKEN, ViewEventNames.CARD_REJECTED,
                    ViewEventNames.GAME_RESTARTED,
                    ModelEventNames.GAME_STARTED, ModelEventNames.BET_MADE,
                    ModelEventNames.CARD_ISSUED, ModelEventNames.GAME_FINISHED,
                    ModelEventNames.GAME_RESTARTED,
                    ]
Observers = dict[EventName, list[Callable[..., None]]]
