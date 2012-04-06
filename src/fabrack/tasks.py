#!/usr/bin/env python

import functools
import os
import sys
from collections import defaultdict

from fabric.api import run, env, sudo, task, runs_once, roles, local

from fabrack.utils import servers, use, create_server_list

env.list_file = 'servers.pkl'
env.public_ip = True
env.servers = []

# Use functools.partial to automatically pass in server list pash
servers = functools.partial(servers, path=env.list_file)

@runs_once
@task
def generate(user='', apikey='', region="US"):
  """Generate a list of servers from the Rackspace Cloud API"""
  if os.path.exists(env.list_file):
    overwrite = raw_input("Overwrite existing server list? (y/n) ")
    if overwrite.lower() != 'y':
      sys.exit(1)
  while user is '' or apikey is '':
    user = raw_input("Rackspace Cloud Username: ")
    apikey = raw_input("Rackspace Cloud API Key: ")

  create_server_list(user, apikey, region, env.list_file)

@runs_once
@task
def list():
  """List Cloud Server name and IP address"""
  if env.servers:
    for info in env.servers:
      print "%s\t%s" % info
  else:
    for host in env.hosts:
      print host

@runs_once
@task
def private():
  """Use internal IP addressing"""
  env.public_ip = False

@runs_once
@task
def all():
  """Use all nodes"""
  match()

@task
def match(name='.*'):
  """Regex match servers from list file"""
  use(servers(name), env.public_ip)

@task
def web():
  """Use all webservers"""
  match('^web')

@task
def db():
  """Use all databases"""
  match('^db')

@task
def uptime():
  """Show uptime and load"""
  run('uptime')
