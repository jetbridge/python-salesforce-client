# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os

import betamax

domain = os.environ.get('SF_DOMAIN', 'domain').encode('utf-8')
access_token = os.environ.get('SF_ACCESS_TOKEN', 'access_token').encode('utf-8')
auth_user_id = os.environ.get('SF_USER_ID', 'user_id').encode('utf-8')
client_id = os.environ.get('SF_CLIENT_ID', 'client_id').encode('utf-8')
client_secret = os.environ.get('SF_CLIENT_SECRET', 'client_secret').encode('utf-8')
# org_id = access_token.split('!', 1)[0]

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.default_cassette_options['record_mode'] = 'once'
    config.define_cassette_placeholder('__DOMAIN__', domain)
    config.define_cassette_placeholder('__ACCESS_TOKEN__', access_token)
    config.define_cassette_placeholder('__USER_ID__', auth_user_id)
    # config.define_cassette_placeholder('__ORG_ID__', org_id)
