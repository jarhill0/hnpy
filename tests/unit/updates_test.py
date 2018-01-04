from hnpy import HackerNews
from hnpy.models import Item, Updates, User

_hn = HackerNews()


class HackerStub:
    def __init__(self):
        self.iterate_list = _hn.iterate_list
        self.item = _hn.item
        self.user = _hn.user


hs = HackerStub()


def test_items():
    up = Updates({'items': [123, 456, 789], 'profiles': []}, hs)
    for item in up.items():
        assert isinstance(item, Item)

    def len_iteration(thing):
        count = 0
        for _ in thing:
            count += 1
        return count

    assert len_iteration(up.items()) == 3
    assert len_iteration(up.items(limit=1)) == 1
    assert len_iteration(up.items(limit=0)) == 0
    assert len_iteration(up.items(limit=-1)) == 0
    assert len_iteration(up.items(limit=5)) == 3
    assert len_iteration(up.items(3)) == 3


def test_profiless():
    up = Updates({'items': [], 'profiles': ['john', 'jack', 'sally']}, hs)
    for prof in up.profiles():
        assert isinstance(prof, User)

    def len_iteration(thing):
        count = 0
        for _ in thing:
            count += 1
        return count

    assert len_iteration(up.profiles()) == 3
    assert len_iteration(up.profiles(limit=1)) == 1
    assert len_iteration(up.profiles(limit=0)) == 0
    assert len_iteration(up.profiles(limit=-1)) == 0
    assert len_iteration(up.profiles(limit=5)) == 3
    assert len_iteration(up.profiles(3)) == 3
