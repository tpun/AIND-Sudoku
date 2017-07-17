import solution
import unittest

# ensure all units satisfy the condition
def verify(values):
    for box in solution.boxes:
        for unit in solution.units[box]:
            digits = [ values[b] for b in unit ]
            unittest.TestCase().assertEqual(sorted(digits), list(solution.possible_values))

puzzle_file = 'sudoku_puzzles.txt'
with open(puzzle_file) as f:
    content = f.readlines()
puzzle_grids = [x.strip() for x in content]

for index, grid in enumerate(puzzle_grids):
    print('Solving ', index, '  ', grid)
    values = solution.solve(grid)
    print('Result  ', index, '  ', ''.join(values.values()))
    verify(values)
    # unittest.TestCase().assertTrue(solution.solved_puzzle(solved_list))
