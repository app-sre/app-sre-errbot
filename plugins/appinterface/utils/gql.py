# pylint: disable=C0103
# pylint: disable=W0601
"""Helper module to interract with GraphQL from app-interface module"""

from utils.gql import GqlApi, get_sha_url


def init(url, token=None):
    """Initialize a GraphQL api"""
    global _gqlapi
    server = get_sha_url(url, token)
    _gqlapi = GqlApi(server, token)
    return _gqlapi
