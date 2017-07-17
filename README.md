# SudokuSolver

The board.py file translates 

  |0|8|0|7|0|6|0|0|0|
  -------------------
  |4|6|7|0|0|9|0|0|0|
  |0|0|0|0|0|0|0|4|0|
  |0|0|4|0|9|7|0|0|0|
  |7|0|1|0|0|0|0|8|4|
  |0|9|0|0|0|0|0|2|0|
  |0|0|0|0|0|2|0|0|0|
  |0|2|9|0|7|0|0|0|0|
  |0|0|0|3|5|0|0|0|6|
  
into a dictionary and a set of constriants.

ac3 (arc consistency) is implemented to show how not all sudoku boards can be solved using ac3 alone.

backtracking search with heursitics like forward checking and minimum remaining value can solve any puzzle, faster.
  
