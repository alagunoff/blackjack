import layers.view.types as ViewTypes
from layers.view import view
import layers.model.types as ModelTypes
from layers.model import model


class Presenter():
    def __init__(self, view: view.View, model: model.Model) -> None:
        self._view = view
        self._subscribe_to_view_events()

        self._model = model
        self._subscribe_to_model_events()

    def _subscribe_to_view_events(self) -> None:
        self._view.on(ViewTypes.EventNames.GAME_STARTED,
                      self._handle_game_start)
        self._view.on(ViewTypes.EventNames.MONEY_DEPOSITED,
                      self._handle_money_deposit)
        self._view.on(ViewTypes.EventNames.BET_MADE, self._handle_bet_make)
        self._view.on(ViewTypes.EventNames.CARD_TAKEN, self._handle_card_take)
        self._view.on(ViewTypes.EventNames.CARD_REJECTED,
                      self._handle_card_reject)
        self._view.on(ViewTypes.EventNames.GAME_RESTARTED,
                      self._handle_game_restart)

    def _handle_game_start(self) -> None:
        self._model.start_game()

    def _handle_money_deposit(self, amount: int) -> None:
        self._model.add_money_to_player(amount)

    def _handle_bet_make(self, amount: int) -> None:
        self._model.make_bet_for_player(amount)

    def _handle_card_take(self) -> None:
        self._model.issue_card_to_player()

    def _handle_card_reject(self) -> None:
        self._model.finish_game()

    def _handle_game_restart(self) -> None:
        self._model.restart_game()

    def _subscribe_to_model_events(self) -> None:
        self._model.on(ModelTypes.EventNames.STATE_UPDATED,
                       self._handle_game_update)

    def _handle_game_update(self, state: ModelTypes.State) -> None:
        self._view.update(state)
