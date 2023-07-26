import random

from Hangman.game_status import GameStatus
from Hangman.invalid_exception_error import InvalidExceptionError


class Game:
    def __init__(self, allowed_misses: int = 6):
        if not 5 <= allowed_misses <= 8:
            raise ValueError('Allowed misses should be between 5 and 8')

        self.allowed_misses = allowed_misses
        self.tries_counter = 0
        self.tried_letters = []
        self.game_status = GameStatus.NOT_STARTED
        self.open_indexes = []

        self.word = ''

    def generate_word(self) -> str:
        words = []
        filename = 'data/WordsStockRus.txt'
        with open(filename, encoding='utf8') as file:
            for item in file:
                words.append(item.rstrip('\n'))

        self.word = random.choice(words)
        self.open_indexes = [False for _ in self.word]
        self.game_status = GameStatus.IN_PROGRESS

        return self.word

    def guess_letter(self, letter: str) -> list:
        if self.tries_counter == self.allowed_misses:
            raise InvalidExceptionError(f'Exceeded max number of misses: {self.allowed_misses}')
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidExceptionError(f'Inappropriate status of game: {self.game_status}')

        open_any = False
        result = []

        for i in range(len(self.word)):
            cur_letter = self.word[i]
            if cur_letter == letter:
                self.open_indexes[i] = True
                open_any = True

            if self.open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append('-')

        if not open_any:
            self.tries_counter += 1

        self.tried_letters.append(letter)

        if self.is_winning():
            self.game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.game_status = GameStatus.LOST

        return result

    def is_winning(self):
        for cur in self.open_indexes:
            if not cur:
                return False
        return True
