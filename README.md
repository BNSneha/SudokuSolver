# SudokuSolver

The board.py file translates "080706000467009000000000040004097000701000084090000020000002000029070000000350006" (for a better visualization - the board below)
  
|   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| 8 |   | 7 |   | 6 |   |   |   |   |
| 4 | 6 | 7 |   |   | 9 |   |   |   |
|   |   |   |   |   |   |   | 4 |   |
|   |   | 4 |   | 9 | 7 |   |   |   |
| 7 |   | 1 |   |   |   |   | 8 | 4 |
|   | 9 |   |   |   |   |   | 2 |   |
|   |   |   |   |   | 2 |   |   |   |
|   | 2 | 9 |   | 7 |   |   |   |   |
|   |   |   | 3 | 5 |   |   |   | 6 |
  
into a dictionary and a set of constriants.

ac3 (arc consistency) is implemented to show how not all sudoku boards can be solved using ac3 alone.

backtracking search with heursitics like forward checking and minimum remaining value can solve any puzzle, faster.
  
