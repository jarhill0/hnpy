from hnpy import HackerNews
from hnpy.models import Item, User

_hn = HackerNews()


class HackerStub:
    def __init__(self):
        self.iterate_list = _hn.iterate_list
        self.item = _hn.item


hs = HackerStub()


def test_link():
    user = User('john', None)
    assert user.link == 'https://news.ycombinator.com/user?id=john'


def test_equality():
    user = User('john', None)

    assert user == user

    assert user == 'john'
    assert 'john' == user

    assert user != 'JOHN'  # should be case sensitive

    user2 = User('john', None)

    assert user == user2


def test_bad_attrs():
    user = User('john', None, {'custom_attr': 'magicvalue'})
    try:
        user.nonexistant_attr
    except AttributeError:
        assert True
    else:
        assert False


def test_name():
    user = User('john', None)
    assert user.name == 'john'


def test_custom_attrs():
    user = User('john', None, {'custom_attr': 'magicvalue'})
    assert user.custom_attr == 'magicvalue'


def test_repr():
    user = User('john', None)
    assert "User('john')" == repr(user)


def test_assigning_vals():
    user = User('john', None, {'name': 'wrongname'})
    assert user.name == 'john'  # should not change to wrongname

    # test html unescape
    user = User('john', None, {'about': 'E&gt;'})
    assert user.about == 'E&gt;'


def test_obj_iterator():
    user = User('john', hs, {'submitted': [4, 5, 6, 7]})
    for thing in user.submitted():
        assert isinstance(thing, Item)

    def len_iteration(thing):
        count = 0
        for _ in thing:
            count += 1
        return count

    assert len_iteration(user.submitted()) == 4
    assert len_iteration(user.submitted(limit=1)) == 1
    assert len_iteration(user.submitted(limit=0)) == 0
    assert len_iteration(user.submitted(limit=-1)) == 0
    assert len_iteration(user.submitted(limit=5)) == 4
    assert len_iteration(user.submitted(4)) == 4
