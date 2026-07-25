class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

 
        board_len = len(board[0])

        #row checker
        for i in board:
            seen = set()
            for j in i:
                if j in seen and j != '.':
                    return False
                
                seen.add(j)
            
        #col checker
        for col_index in range(board_len):
            seen_col = set()
            for row in board:
                item = row[col_index]
                if item != '.' and item in seen_col:
                    return False

                seen_col.add(item)

        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                sub_grid = [row[c:c+3] for row in board[r:r+3]]
                print(sub_grid)
                
                flat_grid = []

                for row in sub_grid:
                    for item in row:
                        if item != '.':
                            flat_grid.append(item)
                
                if len(flat_grid) != len(set(flat_grid)):
                    return False



        
    
        return True