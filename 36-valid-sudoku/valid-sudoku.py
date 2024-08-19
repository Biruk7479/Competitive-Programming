class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        output = True    
        
        # Check rows
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in d:
                        d[board[i][j]] += 1
                    else:
                        d[board[i][j]] = 1
                    if d[board[i][j]] > 1:
                        output = False
                        break
            if not output:
                break
                
        # Check columns
        if output:
            for j in range(9):
                d = {}
                for i in range(9):
                    if board[i][j] != '.':
                        if board[i][j] in d:
                            d[board[i][j]] += 1
                        else:
                            d[board[i][j]] = 1
                        if d[board[i][j]] > 1:
                            output = False
                            break
                if not output:
                    break
        
        # Check 3x3 sub-grids
        if output:
            starts = [(0, 0), (0, 3), (0, 6),
                      (3, 0), (3, 3), (3, 6),
                      (6, 0), (6, 3), (6, 6)]
            
            for m, n in starts:
                d = {}
                for i in range(m, m + 3):
                    for j in range(n, n + 3):
                        if board[i][j] != '.':
                            if board[i][j] in d:
                                d[board[i][j]] += 1
                            else:
                                d[board[i][j]] = 1
                            if d[board[i][j]] > 1:
                                output = False
                                break
                    if not output:
                        break
                if not output:
                    break
        
        return output
