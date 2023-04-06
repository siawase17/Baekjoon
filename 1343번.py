def polyomino(board):
    i = 0  # 문자열 인덱스
    while i < len(board):
        if board[i] == 'X':  # 'X'를 찾으면
            if i+3 < len(board) and board[i+1:i+4] == 'XXX':  # 'XXXX'일 경우
                board = board[:i] + 'AAAA' + board[i+4:]
                i += 4
            elif i+1 < len(board) and board[i+1:i+2] == 'X':  # 'XX'일 경우
                board = board[:i] + 'BB' + board[i+2:]
                i += 2
            else:  # 변환할 수 없는 경우
                return "-1"
        else: # 인덱스값 . 인 경우
            i += 1
    return board

board = input()
result = polyomino(board)
print(result)