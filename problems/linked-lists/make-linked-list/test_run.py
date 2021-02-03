from run import LinkedList


class TestLinkedList:
    def test_it(self):
        items = ["one", "two", "three"]
        it = LinkedList()
        for item in items:
            it.add(item)
        for expected, actual in zip(items, it):
            assert expected == actual.item
        assert True

    def test_it_reverses(self):
        items = ["one", "two", "three"]
        it = LinkedList()
        for item in items:
            it.add(item)
        it.reverse()
        for expected, actual in zip(reversed(items), it):
            assert expected == actual.item
        assert True
