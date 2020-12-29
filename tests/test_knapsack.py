from run import knapsack


class TestKnapsack:
    def test_it(self):
        capacity = 4
        w = [4, 3, 1]
        v = [3_000, 2_000, 1_500]
        assert 3_500 == knapsack(capacity, w, v)
