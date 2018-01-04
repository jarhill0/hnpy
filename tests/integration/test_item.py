from hnpy.models import Item
from .preparation import bm, hn


def test_story():
    story = hn.item(8863)
    with bm.use_cassette('test_story'):
        assert story.by == 'dhouston'
        assert story.descendants == 71
        assert story.id == 8863
        assert 8952 in story.kids(limit=None)
        assert story.score == 110
        assert story.time == 1175714200
        assert story.title == 'My YC app: Dropbox - Throw away your USB drive'
        assert story.type == 'story'
        assert story.url == 'http://www.getdropbox.com/u/2/screencast.html'


def test_job():
    text = ('Justin.tv is the biggest live video site online. We serve hundreds of thousands of video streams a day, '
            'and have supported up to 50k live concurrent viewers. Our site is growing every week, and we just added '
            'a 10 gbps line to our colo. Our unique visitors are up 900% since January.<p>There are a lot of pieces '
            'that fit together to make Justin.tv work: our video cluster, IRC server, our web app, and our monitoring '
            "and search services, to name a few. A lot of our website is dependent on Flash, and we're looking for "
            'talented Flash Engineers who know AS2 and AS3 very well who want to be leaders in the development of our '
            'Flash.<p>Responsibilities<p><pre><code>    * Contribute to product design and implementation '
            'discussions\n    * Implement projects from the idea phase to production\n    * Test and iterate code '
            'before and after production release \n</code></pre>\nQualifications<p><pre><code>    * You should know '
            'AS2, AS3, and maybe a little be of Flex.\n    * Experience building web applications.\n    * A strong '
            'desire to work on website with passionate users and ideas for how to improve it.\n    * Experience '
            "hacking video streams, python, Twisted or rails all a plus.\n</code></pre>\nWhile we're growing rapidly, "
            'Justin.tv is still a small, technology focused company, built by hackers for hackers. Seven of our ten '
            'person team are engineers or designers. We believe in rapid development, and push out new code releases '
            "every week. We're based in a beautiful office in the SOMA district of SF, one block from the caltrain "
            'station. If you want a fun job hacking on code that will touch a lot of people, JTV is for you.<p>Note: '
            'You must be physically present in SF to work for JTV. Completing the technical problem at '
            '<a href=\"http://www.justin.tv/problems/bml\" rel=\"nofollow\">http://www.justin.tv/problems/bml</a> '
            'will go a long way with us. Cheers!')

    job = hn.item(192327)
    with bm.use_cassette('test_job'):
        assert job.by == 'justin'
        assert job.id == 192327
        assert job.score == 6
        assert job.text == text
        assert job.time == 1210981217
        assert job.title == 'Justin.tv is looking for a Lead Flash Engineer!'
        assert job.type == 'job'
        assert job.url == ''


def test_comment():
    text = ("Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep "
            'writing if you keep reading. K?')

    comment = hn.item(2921983)
    with bm.use_cassette('test_comment'):
        assert comment.by == 'norvig'
        assert comment.id == 2921983
        assert 2924562 in comment.kids(limit=None)
        assert comment.parent == 2921506
        assert comment.text == text
        assert comment.time == 1314211127
        assert comment.type == 'comment'


def test_poll():
    poll = hn.item(126809)
    with bm.use_cassette('test_poll'):
        assert poll.by == 'pg'
        assert poll.descendants == 54
        assert poll.id == 126809
        assert 126822 in poll.kids(limit=None)
        assert 126810 in poll.parts(limit=None)
        assert poll.score == 47
        assert poll.time == 1204403652
        assert poll.title == 'Poll: What would happen if News.YC had explicit support for polls?'
        assert poll.type == 'poll'


def test_pollopt():
    pollopt = hn.item(160705)
    with bm.use_cassette('test_pollopt'):
        assert pollopt.by == 'pg'
        assert pollopt.id == 160705
        assert pollopt.poll == 160704
        assert pollopt.score == 335
        assert pollopt.text == "Yes, ban them; I'm tired of seeing Valleywag stories on News.YC."
        assert pollopt.time == 1207886576
        assert pollopt.type == 'pollopt'


def test_lazy_loading():
    item = hn.item(16072368)
    assert 'by' not in vars(item)
    with bm.use_cassette('test_lazy_loading'):
        item.title
    assert hasattr(item, 'by')


def test_iter_first():
    story = hn.item(8863)
    with bm.use_cassette('test_item_iter_first'):
        for kid in story.kids(limit=5):
            assert isinstance(kid, Item)
