#!/usr/bin/env python

import boto.opsworks.layer1 as opsworks
import os
import argparse


conn   = opsworks.OpsWorksConnection()

def display_intro():
  print '\nfofops - connect to your amazon opsworks instances'

def get_input_from_choices(choices, header, entity):
  print '\n%s\n------------------------------------------------' % header
  for k, v in choices.iteritems(): print '%2s - %s' % (k, v)
  print ' 0 - exit'

  try:
    num = int(raw_input('\nChoose an %s: ' % entity))
  except:
    num = -1
    pass

  if num > 0 and num <= len(choices):
    return choices[num]
  elif num is 0:
    os._exit(0)

def get_stack():
  stacks = dict([(s['Name'], s) for s in conn.describe_stacks()['Stacks']])
  stack_names = dict([(i+1, s) for (i, s) in enumerate(stacks.keys())])

  stack = None
  while not stack:
    stack = get_input_from_choices(stack_names, 'stacks:', 'stack')

  return stacks[stack]

def get_instance(stack):
  stack_id = stack['StackId']
  raw_instances = conn.describe_instances(stack_id)['Instances']
  instances = dict([(ins['Hostname'], ins) \
    for ins in raw_instances if ins['Status'] == 'online'])
  instance_names = dict([(i+1, ins) \
    for (i, ins) in enumerate(instances.keys())])

  instance = None
  while not instance:
    instance = get_input_from_choices(instance_names, 'instances:', 'instance')

  return instances[instance]

def main(ssh_args=''):
  display_intro()
  while True:
    stack = get_stack()
    instance = get_instance(stack)
    if 'PublicDns' in instance:
      _ssh(instance['PublicDns'], args=ssh_args)
    elif 'PrivateIp' in instance:
      _ssh(instance['PrivateIp'], args=ssh_args)
    else:
      print instance

def _ssh(ip='', args=''):
  if args:
    os.system('ssh %s %s' % (args, ip))
  else:
    os.system('ssh %s' % ip)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-ssh-opts', '--ssh-opts', dest='ssh_args')
  args = parser.parse_args()
  main(ssh_args=args.ssh_args)
