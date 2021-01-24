from GamePlayer import PlayGame
from Classes import Vile

COLORS = {
    1: 'green',
    2: 'lightblue',
    3: 'darkgreen',
    4: 'blue',
    5: 'orange',
    6: 'purple',
    7: 'gray',
    8: 'pink',
    9: 'lightgreen',
    10: 'brown',
    11: 'red',
    12: 'yellow'
}

GAME_BOARD = [
    Vile(1, 2, 3, 4),
    Vile(2, 5, 3, 2),
    Vile(5, 4, 6, 7),
    Vile(8, 8, 9, 5),
    Vile(6, 9, 9, 1),
    Vile(10, 11, 4, 12),
    Vile(6, 10, 4, 3),
    Vile(12, 12, 7, 1),
    Vile(8, 3, 1, 6),
    Vile(11, 12, 10, 8),
    Vile(7, 9, 10, 11),
    Vile(5, 2, 11, 7),
    Vile(None, None, None, None),
    Vile(None, None, None, None)
]


def main():
    PlayGame(GAME_BOARD)


if __name__ == '__main__':
    main()
