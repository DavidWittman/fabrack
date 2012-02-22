#!/usr/bin/env/python

import os
import pickle
import re
import sys

import cloudservers
from fabric.api import env

def create_server_list(user, apikey, region, path):
  """Creates a full list of Rackspace Cloud Servers"""
  cs = cloudservers.CloudServers(user, apikey)
  servers = []
  for server in cs.servers.list():
    servers.append({ 'name': server.name, 'addresses': server.addresses })
  try:
    fh = open(path, 'w')
    pickle.dump(servers, fh)
    fh.close()
  except IOError, e:
    print "Error saving server list."
    sys.exit(1)

def get_server_list(path):
  try:
    fh = open(path, 'r')
    servers = pickle.load(fh)
    fh.close()
  except IOError, e:
    print "Error reading server list %s." % path
    sys.exit(1)
  return servers

def servers(match, path):
  regex = re.compile(match, flags=re.IGNORECASE)
  servers = []
  for server in get_server_list(path):
    if regex.search(server['name']):
      servers.append(server)
  return servers

def use(servers, public_ip=True):
  ip_type = public_ip is True and "public" or "private"
  for server in servers:
    env.servers.append((server['addresses'][ip_type][0], server['name']))
    env.hosts.append(server['addresses'][ip_type][0])
