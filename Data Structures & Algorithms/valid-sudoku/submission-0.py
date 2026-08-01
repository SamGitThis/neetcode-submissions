class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] in rows:
                    return False
                if board[i][j] == ".":
                    continue
                else:
                    rows.add(board[i][j])

        for i in range(9):
            cols = set()
            for j in range(9):
                if board[j][i] in cols:
                    return False
                if board[j][i] == ".":  
                    continue
                else:
                    cols.add(board[j][i])

        for sq in range(9):
            sqs = set()
            for r in range(3):
                for c in range(3):
                    row = (sq // 3) * 3 + r
                    col = (sq % 3) * 3 + c

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sqs:
                        return False
                    else:
                        sqs.add(board[row][col])

        
        return True



