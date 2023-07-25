from Hangman.game import Game
from Hangman.game_status import GameStatus


def chars_to_word(lst):
    return ''.join(lst)


game = Game()
word = game.generate_word()

print(f'The word consists of {len(word)} letters')
print('Try to guess the word letter by letter')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter\n')
    state = game.guess_letter(letter)
    print(chars_to_word(state))

    print(f'Remaining tries: {game.allowed_misses - game.tries_counter}')
    print(f'Used letters are {chars_to_word(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
    print('You lose')
    print(f'The word was {word}')
else:
    print('Congrats! You are winner')
