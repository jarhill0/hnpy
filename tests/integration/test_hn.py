from hnpy.models import Item
from .preparation import bm, hn


def test_ask():
    with bm.use_cassette('test_ask'):
        it = hn.ask(limit=3)
    assert next(it) == 16073801
    assert next(it) == 16072147
    assert next(it) == 16072185


def test_best():
    with bm.use_cassette('test_best'):
        it = hn.best(limit=3)
    assert next(it) == 16065845
    assert next(it) == 16060855
    assert next(it) == 16057449


def test_jobs():
    with bm.use_cassette('test_jobs'):
        it = hn.jobs(limit=3)
    assert next(it) == 16072624
    assert next(it) == 16069255
    assert next(it) == 16068520


def test_max_item():
    with bm.use_cassette('test_max_item'):
        assert hn.max_item() == 16073872
        assert isinstance(hn.max_item(), Item)


def test_new():
    with bm.use_cassette('test_new'):
        it = hn.new(limit=3)
    assert next(it) == 16074223
    assert next(it) == 16074220
    assert next(it) == 16074211


def test_show():
    with bm.use_cassette('test_show'):
        it = hn.show(limit=3)
    assert next(it) == 16070394
    assert next(it) == 16070949
    assert next(it) == 16072417


def test_top():
    with bm.use_cassette('test_top'):
        it = hn.top(limit=3)
    assert next(it) == 16073874
    assert next(it) == 16072368
    assert next(it) == 16073745
