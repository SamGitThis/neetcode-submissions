class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rn, cn = len(board), len(board[0])
        n = len(word)
        
        if rn == cn == 1:
            if board[0][0] == word:
                return True
            return False
        
        def backtrack(r, c, index):
            if index == n:
                return True
            
            if board[r][c] != word[index]:
                return False
            
            #Everything below indicates that there is a match.
            char = board[r][c]
            board[r][c] = '#'
            
            for i, j in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= r+i < rn and 0 <= c+j < cn:
                    if backtrack(r+i, c+j, index+1):
                        return True
            
            board[r][c] = char
            return False
        
        for i in range(rn):
            for j in range(cn):
                if backtrack(i, j, 0): return True
                
        return False