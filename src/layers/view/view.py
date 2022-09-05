from observable import Observable
from layers.model import State, GameStages, PlayerNames, MIN_BET

from .constants import WINNER_TO_DISPLAYED_WINNER, MESSAGES, AFFIRMATIVE_PLAYER_ANSWERS, RUBLE_SIGN
from .types import EventNames


class View(Observable):
    def update(self, model_state: State) -> None:
        match model_state['game']['stage']:
            case GameStages.FIRST_STARTING_IS_AWAITED:
                print(MESSAGES['welcome'])
                self._request_first_game_starting()
            case GameStages.STARTING_IS_AWAITED:
                self._request_game_starting()
            case GameStages.DEPOSIT_IS_AWAITED:
                self._request_deposit()
            case GameStages.BET_IS_AWAITED:
                self._print_bet_request_preview(
                    model_state['statistics'][PlayerNames.PLAYER.value]['money'])
                self._request_bet(
                    model_state['statistics'][PlayerNames.PLAYER.value]['money'])
            case GameStages.CARD_TAKING_IS_AWAITED:
                self._print_card_taking_request_preview(model_state)
                self._request_card_taking()
            case GameStages.FINISHED:
                self._print_game_result(model_state)
                self._request_game_restart()
            case _:
                pass

    def _request_first_game_starting(self) -> None:
        if self._check_if_player_answer_affirmative(input(MESSAGES['try_luck'])):
            self.emit(EventNames.GAME_STARTED)

    def _request_game_starting(self) -> None:
        if self._check_if_player_answer_affirmative(input(MESSAGES['one_more_game'])):
            self.emit(EventNames.GAME_STARTED)

    def _request_deposit(self) -> None:
        while True:
            deposit = input(MESSAGES['deposit'])

            if deposit.isdigit():
                break

        self.emit(EventNames.MONEY_DEPOSITED, int(deposit))

    def _request_bet(self, player_money: int) -> None:
        while True:
            bet = input(
                f'Твоя ставка(мин. {MIN_BET}{RUBLE_SIGN}, макс. {player_money}{RUBLE_SIGN}): ')

            if bet.isdigit():
                bet_as_int = int(bet)

                if MIN_BET <= bet_as_int <= player_money:
                    break

        self.emit(EventNames.BET_MADE, bet_as_int)

    def _request_card_taking(self) -> None:
        if self._check_if_player_answer_affirmative(input(MESSAGES['one_more_card'])):
            self.emit(EventNames.CARD_TAKEN)
        else:
            self.emit(EventNames.CARD_REJECTED)

    def _request_game_restart(self) -> None:
        if self._check_if_player_answer_affirmative(input(MESSAGES['one_more_time'])):
            self.emit(EventNames.GAME_RESTARTED)

    def _check_if_player_answer_affirmative(self, answer: str) -> bool:
        return answer in AFFIRMATIVE_PLAYER_ANSWERS

    def _print_bet_request_preview(self, player_money: int) -> None:
        print(f'''
===================
Твои деньги: {player_money}{RUBLE_SIGN}
===================
''')

    def _print_card_taking_request_preview(self, model_state: State) -> None:
        print(f'''
===================
Банк: {model_state['game']['bank']}{RUBLE_SIGN}
-------------------
Твои деньги: {model_state['statistics'][PlayerNames.PLAYER.value]['money']}{RUBLE_SIGN}
Твои карты: {model_state['game'][PlayerNames.PLAYER.value]['deck']}
Твои очки: {model_state['game'][PlayerNames.PLAYER.value]['score']}
===================
''')

    def _print_game_result(self, model_state: State) -> None:
        winner = model_state['game']['winner']

        print(f'''
===================
Победитель: {WINNER_TO_DISPLAYED_WINNER[winner.value if winner else 'draw']}
-------------------
Твой результат:
  Карты: {model_state['game'][PlayerNames.PLAYER.value]['deck']}
  Очки: {model_state['game'][PlayerNames.PLAYER.value]['score']}
  Деньги: {model_state['statistics'][PlayerNames.PLAYER.value]['money']}{RUBLE_SIGN}
  Выигрышей за все время: {model_state['statistics'][PlayerNames.PLAYER.value]['wins']}
-------------------
Результат Skynet:
  Карты: {model_state['game'][PlayerNames.COMPUTER.value]['deck']}
  Очки: {model_state['game'][PlayerNames.COMPUTER.value]['score']}
  Выигрышей за все время: {model_state['statistics'][PlayerNames.COMPUTER.value]['wins']}
===================
''')
