class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue
                boardIndex = (j // 3) + (3 * (i // 3))
                if num in rows[i] or num in cols[j] or num in boxes[boardIndex]:
                    return False
                rows[i][num] = cols[j][num] = boxes[boardIndex][num] = True

        return True
        