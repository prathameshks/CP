def game_status(board_size, board):
    bc_old = 0
    rc_old = 0
    ec_old = 0
    data = []
    for i in range(board_size):
        bc,rc,ec=0,0,0
        for j in board[i]:
            if j in ('r', 'R'):
                rc += 1
            elif j in ('b','B'):
                bc+=1
            else:
                ec+=1
        data.append((bc,rc,ec))
        bc_old += bc
        rc_old += rc
        ec_old += ec
    if abs(bc_old-rc_old) > 1 or bc_old>=2*board_size or rc_old>2*board_size:
        return 'Impossible'
    else:
        for a in data:
            if a[0]==board_size:
                return 'Blue wins'
            elif a[1]==board_size:
                return 'Red wins'
        
        else:
            return "Nobody wins"

def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        board_size = int(input())
        board = []
        for _ in range(board_size):
            board.append(list(input().strip()))

        ans = game_status(board_size, board)

        print("Case #{}: {}".format(test_case, ans))
if __name__ == "__main__":
    main()
