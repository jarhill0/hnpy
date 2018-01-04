from .preparation import bm, hn


def test_user():
    user = hn.user('jl')
    with bm.use_cassette('test_user'):
        assert user.about == "This is a test"
        assert user.created == 1173923446
        assert user.id == "jl"
        assert user.karma == 3521
        assert 14237416 in user.submitted(limit=None)
