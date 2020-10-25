board = {
    'top-l': '-----', 'top-m': '-----', 'top-r': '-----',
    'mid-l': '-----', 'mid-m': '-----', 'mid-r': '-----',
    'bottom-l': '-----', 'bottom-m': '-----', 'bottom-r': '-----',
}


def printBoard(uBoard):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print(board['bottom-l'] + '|' + board['bottom-m'] + '|' + board['bottom-r'])


turn = '--X--'
printBoard(board)
for i in range(10):
    move = input(turn + ' move' + ' where to move.')
    board[move] = turn
    printBoard(board)

    if turn == '--X--':
        turn = '--O--'
    else:
        turn = '--X--'
