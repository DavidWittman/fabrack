#!/usr/bin/env/python

import os
import os.path
import pickle
import re
import sys

import novaclient
from fabric.api import env

us_authurl_v1_0 = "https://auth.api.rackspacecloud.com/v1.0"
uk_authurl_v1_0 = "https://lon.auth.api.rackspacecloud.com/v1.0"

us_authurl_v1_1 = "https://auth.api.rackspacecloud.com/v1.1"
uk_authurl_v1_1 = "https://lon.auth.api.rackspacecloud.com/v1.1"

us_authurl_v2_0 = "https://auth.api.rackspacecloud.com/v2.0/tokens"
uk_authurl_v2_0 = "https://lon.auth.api.rackspacecloud.com/v2.0/tokens"

def create_server_list(user, apikey, region=None, path=os.path.expanduser('~/.fabrackservers'):
  """Creates a full list of Rackspace Cloud Servers
  Region"""
  if region == 'uk':
    auth = uk_authurl_v1_0
  else:
    auth = us_authurl_v1_0
  cs = novaclient.v1_0.client.Client(user, apikey, None, auth)
  servers = []
  for server in cs.servers.list():
    servers.append({ 'name': server.name, 'addresses': server.addresses })
  with open(path, 'w') as fh:
    pickle.dump(servers, fh)
  return servers

def get_server_list(path=os.path.expanduser('~/.fabrackservers')):
  with open(path, 'r') as fh:
    servers = pickle.load(fh)
  return servers

def make_roles(rdict, path, public_ip=False):
  """Setup Fabric to create role definitions so @role('something') works"""
  servers = get_server_list(path)
  ip_type = public_ip is True and "public" or "private"
  for key in rdict.keys():
    env.roledefs[key] = []
  env.roledefs['all'] = []
  for server in servers:
    for (key, value) in rdict.iteritems():
      if value in server['name']:
        env.roledefs[key].append(server['addresses'][ip_type][0])
        env.roledefs['all'].append(servers['addresses'][ip_type][0])

#def servers(match, path):
#  regex = re.compile(match, flags=re.IGNORECASE)
#  servers = []
#  for server in get_server_list(path):
#    if regex.search(server['name']):
#      servers.append(server)
#  return servers

#def use(servers, public_ip=True):
#  ip_type = public_ip is True and "public" or "private"
#  for server in servers:
#    env.servers.append((server['addresses'][ip_type][0], server['name']))
#    env.hosts.append(server['addresses'][ip_type][0])
