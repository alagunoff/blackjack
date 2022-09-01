from savings import Savings
from layers.view.view import View
from layers.presenter.presenter import Presenter
from layers.model.model import Model


class BlackJack:
    def __init__(self) -> None:
        self._view = View()
        self._model = Model()
        self._savings = Savings(self._model)
        self._presenter = Presenter(self._view, self._model)

        saved_game = self._savings.load_game()

        if saved_game:
            self._model.update_game_state(saved_game)

        self._view.update(self._model.get_game_state())


BlackJack()
