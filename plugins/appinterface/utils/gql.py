from utils.gql import GqlApi, get_sha_url


def init(url, token=None):
    global _gqlapi
    server = get_sha_url(url, token)
    _gqlapi = GqlApi(server, token)
    return _gqlapi
