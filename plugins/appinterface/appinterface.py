"""This is an errbot module to interract with app-interface"""

import os

from itertools import chain

from errbot import BotPlugin, botcmd

from reconcile import queries

from utils import gql


CONFIG_TEMPLATE = {
    'gql_server': 'http://graphql.example.com:4000',
    'gql_token': 'example',
}


class AppInterface(BotPlugin):  # pylint: disable=too-many-ancestors
    """Query app-interface information."""

    def configure(self, configuration):
        config = {}

        server = os.getenv('GQL_SERVER', None)
        if server:
            config['gql_server'] = server

        token = os.getenv('GQL_TOKEN', None)
        if token:
            config['gql_token'] = token

        config = dict(chain(CONFIG_TEMPLATE.items(),
                            config.items()))

        super(AppInterface, self).configure(config)

    def get_configuration_template(self):
        return CONFIG_TEMPLATE

    @botcmd(split_args_with=None, template='ai_find_user')
    def ai_find_user(self, _, args):
        """Find users in app-interface"""

        if len(args) < 1:
            return "Must supply a search argument"

        term = args[0].lower()
        if len(term) < 3:
            return f"Search term '{term}' is too short (min 3 characters)"

        server = self.config['gql_server']
        token = self.config['gql_token']
        gql.init(server, token)
        users = queries.get_users()

        found = []
        for user in users:
            if term in user['org_username'].lower() or \
               term in user['name'].lower():
                found.append(user)
                continue

        if len(found) > 50:
            return (
                f"Search for term '{term}' returned more than 50 results. "
                f"Please refine your search"
            )

        if len(found) == 0:
            return f"No user found matching term '{term}'"

        return {'users': found}

    @botcmd(split_args_with=None, template='ai_get_user')
    def ai_get_user(self, _, args):
        """Show a single user from app-interface"""

        if len(args) < 1:
            return "Must supply a search argument"

        term = args[0].lower()

        server = self.config['gql_server']
        token = self.config['gql_token']
        gql.init(server, token)
        users = queries.get_users()

        found = None
        for user in users:
            if term == user['org_username'].lower():
                found = user
                break

        if not found:
            return f"User {term} not found."

        return {'user': found}

    @botcmd(split_args_with=None, template='ai_find_cluster')
    def ai_find_cluster(self, _, args):
        """Search clusters registered in app-interface"""

        if len(args) < 1:
            return "Must supply a search argument"

        term = args[0].lower()
        if len(term) < 3:
            return f"Search term '{term}' is too short (min 3 characters)"

        server = self.config['gql_server']
        token = self.config['gql_token']
        gql.init(server, token)
        clusters = queries.get_clusters()

        found = []
        for cluster in clusters:
            if term in cluster['name'].lower():
                found.append(cluster)

        if len(found) == 0:
            return f"No clusters found for term '{term}'."

        return {'clusters': found}

    @botcmd(split_args_with=None, template='ai_get_cluster')
    def ai_get_cluster(self, _, args):
        """Show a single cluster from app-interface"""

        if len(args) < 1:
            return "Must supply a search argument"

        term = args[0].lower()

        server = self.config['gql_server']
        token = self.config['gql_token']
        gql.init(server, token)
        clusters = queries.get_clusters()

        found = None
        for cluster in clusters:
            if term == cluster['name'].lower():
                found = cluster
                break

        if not found:
            return f"Cluster {term} not found."

        return {'cluster': found}

    @botcmd(split_args_with=None, template='ai_find_namespace')
    def ai_find_namespace(self, _, args):
        """Search namespaces registered in app-interface"""

        if len(args) < 1:
            return "Must supply a search argument"

        term = args[0].lower()
        if len(term) < 3:
            return f"Search term '{term}' is too short (min 3 characters)"

        server = self.config['gql_server']
        token = self.config['gql_token']
        gql.init(server, token)
        namespaces = queries.get_namespaces()

        found = []
        for namespace in namespaces:
            if term in namespace['name'].lower():
                found.append(namespace)

        if len(found) == 0:
            return f"No namespaces found for term '{term}'."

        return {'namespaces': found}

    @botcmd(split_args_with=None, template='ai_find_app')
    def ai_find_app(self, _, args):
        """Search apps registered in app-interface"""

        if len(args) < 1:
            return "Must supply a search argument"

        term = args[0].lower()
        if len(term) < 3:
            return f"Search term '{term}' is too short (min 3 characters)"

        server = self.config['gql_server']
        token = self.config['gql_token']
        gql.init(server, token)
        apps = queries.get_apps()

        found = []
        for app in apps:
            if term in app['name'].lower():
                found.append(app)

        if len(found) == 0:
            return f"No apps found for term '{term}'."

        return {'apps': found}
