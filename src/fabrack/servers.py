#!/usr/bin/env python

import functools
import os
import os.path
import sys
from collections import defaultdict

from fabric.api import run, env, sudo, task, runs_once, roles, local

from fabrack.utils import create_server_list, get_server_list

@runs_once
@task
def generate(user='', apikey='', region="US"):
  """Generate a list of servers from the Rackspace Cloud API"""
  if os.path.exists(env.servers_path):
    overwrite = raw_input("Overwrite existing server list? (y/n) ")
    if overwrite.lower() != 'y':
      sys.exit(1)
  while user is '' or apikey is '':
    user = raw_input("Rackspace Cloud Username: ")
    apikey = raw_input("Rackspace Cloud API Key: ")

  create_server_list(user, apikey, region)

@runs_once
@task
def list():
  """List Cloud Server name and IP address"""
  servers = get_server_list()
  for server in servers:
      print "%30s\t%16s\t%s" % (server['name'], 
         server['addresses']['public'][0], server['addresses']['private'][0])

@runs_once
@task
def private():
  """Use internal IP addressing"""
  env.public_ip = False
