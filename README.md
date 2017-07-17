# SudokuSolver

The board.py file translates 
  080706000
  467009000
  000000040
  004097000
  701000084
  090000020
  000002000
  029070000
  000350006
into a dictionary and a set of constriants.

ac3 (arc consistency) is implemented to show how not all sudoku boards can be solved using just ac3 alone.

Backtracking search with heursitics like forward checking and minimum remaining value can solve any puzzle, faster.
  
