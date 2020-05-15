from dlgo.goboard_slow import Board, GameState
from dlgo.gotypes import Point


def is_point_an_eye(board :Board, point: Point, color):

    # 目は空の点
    if board.get(point) is not None:
        return False

    # 隣接するすべての点には味方の石が含まれている必要がある
    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False

    # 点が盤の中央にある場合、４つの角のうち３つの角を支配する必要がある
    # 辺ではすべての角を支配する必要がある
    friendly_corners = 0
    off_board_corners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1
        else:
            off_board_corners += 1

    if off_board_corners > 0:
        # 点が角または辺にある
        return off_board_corners + friendly_corners == 4

    # 点は中央にある
    return friendly_corners >= 3
