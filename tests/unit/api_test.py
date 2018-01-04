import hnpy

hn = hnpy.HackerNews()


def test_return_types():
    user = hn.user('testuser')
    assert isinstance(user, hnpy.models.User)

    item = hn.item(12345)
    assert isinstance(item, hnpy.models.Item)


def test_custom_base_path():
    path = 'https://example.com/'
    hn_ = hnpy.HackerNews(base_path=path)  # with keyword
    assert hn_.base_path == path

    hn_ = hnpy.HackerNews(path)  # without keyword
    assert hn_.base_path == path
