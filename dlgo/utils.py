from dlgo import gotypes
from dlgo.goboard_slow import Move
from dlgo.gotypes import Player

COLS = 'ABCDEFGHIJKLMNOPQRST'
STONE_TO_CHAR = {
    None: '　',
    gotypes.Player.black: '●',
    gotypes.Player.white: '○',
}

def print_move(player :Player, move: Move):
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = f"{COLS[move.point.col - 1]}{move.point.row}"
    print(f"{player} {move_str}")

def print_board(board):
    for row in range(board.num_rows, 0, -1):
        bump = " " if row <= 9 else ""
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print(f"{bump}{row} {''.join(line)}")
    print('    ' + ' '.join(COLS[:board.num_cols]))