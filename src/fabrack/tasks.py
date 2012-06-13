#!/usr/bin/python

from fabric.api import run, env, sudo, task, runs_once, roles, local

@task
def uptime(role):
  """Show uptime and load"""
  with settings(roles=role):
    run('uptime')
