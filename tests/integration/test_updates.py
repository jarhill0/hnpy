from .preparation import bm, hn


def test_updates():
    with bm.use_cassette('test_updates'):
        updates = hn.updates()
    assert 16073931 in updates.items(limit=None)
    assert 'coliveira' in updates.profiles(limit=None)
