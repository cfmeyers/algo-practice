"""
0/1 Knapsack Problem
See https://www.askpython.com/python/examples/knapsack-problem-dynamic-programming#problem-statement-for-0/1-knapsack
"""
from typing import List


def ppt(grid):
    print(list(range(len(grid[0]))))
    print("------------")
    for i in range(len(grid)):
        print(grid[i])


"""
 [0     1     2     3     4   ]
 -----------------------------
 [0,    0,    0,    0,    0   ]
 [0,    0,    0,    0,    3000]
 [0,    0,    0,    2000, 3000]
 [0,    1500, 1500, 2000, 3500]
"""


def knapsack(capacity: int, weights: List[int], vals: List[int]):
    """
    capacity is the max weight your knapsack can hold
    weights is the vector of weights of items
    vals is the vector of values of items
    """
    num_vals = len(vals)

    # create a capacity x num_vals solution matrix to store the sub-problem results
    grid = [[0 for _ in range(capacity + 1)] for _ in range(num_vals + 1)]

    for i in range(num_vals + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                grid[i][j] = 0
                continue

            item_idx = i - 1
            previous_max = grid[i - 1][j]  # the previous max for given weight class
            item_weight = weights[item_idx]  # the current item's weight
            item_val = vals[item_idx]  # the current item's value

            if item_weight <= j:
                val_with_cur_item = item_val + grid[i - 1][j - item_weight]
                grid[i][j] = max(previous_max, val_with_cur_item)
            else:
                grid[i][j] = previous_max

    return grid[num_vals][capacity]
