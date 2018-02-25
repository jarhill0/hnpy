from hnpy import HackerNews
from hnpy.models import Item, User

_hn = HackerNews()


class HackerStub:
    def __init__(self):
        self.iterate_list = _hn.iterate_list
        self.user = _hn.user
        self.item = _hn.item


hs = HackerStub()


def test_repr():
    item = Item(123, None)
    assert repr(item) == 'Item(123)'


def test_equality():
    story_int = Item(123, None)
    story_str = Item("123", None)

    assert story_int == story_int
    assert story_str == story_str

    assert story_int == 123
    assert story_int == "123"

    assert story_str == "123"
    assert story_str == 123

    assert story_str == story_int


def test_custom_data():
    item = Item(123, None, {'custom_attr': 'magicvalue'})
    assert item.custom_attr == 'magicvalue'
    try:
        item.nonexistant_attr
    except AttributeError:
        assert True
    else:
        assert False

    # we shouldn't be able to change the ID.
    item = Item(123, None, {'id': 456})
    assert item.id == 123

    # special "object iterators" should return objects
    item = Item(123, hs, {'kids': [123, 456, 789], 'parts': [987, 654, 321]})
    for kid in item.kids():
        assert isinstance(kid, Item)
    for part in item.parts():
        assert isinstance(part, Item)

    # special "object attributes" should return objects
    item = Item(123, hs, {'by': 'magicspiders', 'parent': 456, 'poll': 789})
    assert isinstance(item.parent, Item)
    assert isinstance(item.poll, Item)
    assert isinstance(item.by, User)


def test_iterators():
    def len_iteration(thing):
        count = 0
        for _ in thing:
            count += 1
        return count

    item = Item(123, hs, {'kids': [1, 2, 3]})
    assert len_iteration(item.kids()) == 3
    assert len_iteration(item.kids(limit=1)) == 1
    assert len_iteration(item.kids(limit=0)) == 0
    assert len_iteration(item.kids(limit=-1)) == 0
    assert len_iteration(item.kids(limit=5)) == 3
    assert len_iteration(item.kids(3)) == 3

    item = Item(123, hs, {'parts': [1, 2, 3]})
    assert len_iteration(item.parts()) == 3
    assert len_iteration(item.parts(limit=1)) == 1
    assert len_iteration(item.parts(limit=0)) == 0
    assert len_iteration(item.parts(limit=-1)) == 0
    assert len_iteration(item.parts(limit=5)) == 3
    assert len_iteration(item.parts(3)) == 3


def test_escape():
    item = Item(123, None, {'text': '&lt;3'})
    assert item.text == '&lt;3'


def test_content():
    no_content = Item(123, None, data={'dummy': ''})
    assert no_content.content == ''

    only_title = Item(123, None, data={'title': 'hello'})
    assert only_title.content == 'hello'

    title_and_url = Item(123, None, data={'title': 'hello', 'url': 'https://github.com'})
    assert title_and_url.content == 'https://github.com'

    all_three = Item(123, None, data={'title': 'hello', 'url': 'https://github.com', 'text': 'main'})
    assert all_three.content == 'main'


def test_link():
    story1 = Item(16071290, None)
    story2 = Item('16071290', None)

    assert story1.link == 'https://news.ycombinator.com/item?id=16071290' == story2.link
