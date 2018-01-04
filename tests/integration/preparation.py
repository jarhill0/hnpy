from betamax import Betamax
from betamax_serializers.pretty_json import PrettyJSONSerializer
from requests import Session

from hnpy import HackerNews

with Betamax.configure() as config:
    config.cassette_library_dir = 'tests/integration/cassettes'

Betamax.register_serializer(PrettyJSONSerializer)

session = Session()
hn = HackerNews(session=session)
bm = Betamax(session, default_cassette_options={'serialize_with': 'prettyjson'})
