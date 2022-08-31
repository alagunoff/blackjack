from pathlib import Path
import os
import json

from layers.model import Game


class Saver:
    def __init__(self) -> None:
        self._savings_file_path = f'{Path(__file__).parent}/savings.json'

    def save_game(self, game: Game) -> None:
        if self._check_if_savings_file_exists():
            self._update_savings_file(game)
        else:
            self._create_savings_file(game)

    def _create_savings_file(self, game: Game) -> None:
        with open(self._savings_file_path, 'w', encoding='utf-8') as savings_file:
            json.dump([game], savings_file)

    def _update_savings_file(self, game: Game) -> None:
        with open(self._savings_file_path, 'r', encoding='utf-8') as savings_file:
            savings = json.load(savings_file)
            savings.insert(0, game)
        with open(self._savings_file_path, 'w', encoding='utf-8') as savings_file:
            json.dump(savings, savings_file)

    def _check_if_savings_file_exists(self) -> bool:
        return os.path.exists(self._savings_file_path)
