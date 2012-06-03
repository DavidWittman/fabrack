#!/usr/bin/python

import os
import os.path
import sys
import pprint

from fabric.api import run, env, sudo, task, runs_once, roles, local

import fabrack.servers as servers
import fabrack.tasks as rack

from fabrack.utils import make_roles

env.public_ip = True
env.servers_path = os.path.expanduser('~/.fabrackservers')
# in rdict, key => @role name :: value => search term
env.rdict = {'web': 'web', 'db': 'db', 'cache': 'varnish'}

if not os.path.exists(env.servers_path):
    servers.generate()
make_roles(env.rdict)

pprint(env.roledefs)


