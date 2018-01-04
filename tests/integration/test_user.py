from hnpy.models import Item
from .preparation import bm, hn


def test_user():
    user = hn.user('jl')
    with bm.use_cassette('test_user'):
        assert user.about == "This is a test"
        assert user.created == 1173923446
        assert user.id == "jl"
        assert user.karma == 3521
        assert 14237416 in user.submitted(limit=None)


def test_nonexistent_user():
    user = hn.user('JOHN')
    with bm.use_cassette('test_nonexistent_user'):
        try:
            user.karma
        except ValueError:
            assert True
        else:
            assert False


def test_iter_first():
    user = hn.user('jl')
    with bm.use_cassette('test_user_iter_first'):
        for submitted in user.submitted(limit=5):
            assert isinstance(submitted, Item)
