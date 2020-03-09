#!/usr/bin/python
"""
Tool to analyze the certifices present in one or more apks, including
any nested apks within resources.

Usage: ./apk_emoji_certs.py <apk_path> ...
"""

import sys
import tempfile
import shutil
import pipes
import os
import subprocess
import re


def Usage():
  print __doc__
  sys.exit(1)


def Fail(msg):
  print '*** Error: %s' % msg
  sys.exit(1)


def AnalyzeApk(apk_path, apk_rel_path=None, prefix=''):
  name = apk_path
  if apk_rel_path is not None:
    name = apk_rel_path
  print
  print prefix + name
  tmp_dir = tempfile.mkdtemp()
  try:
    if os.system('unzip -q %s -d %s' % (
        pipes.quote(apk_path), pipes.quote(tmp_dir))):
      Fail('Could not unzip apk')
    rsa_file = os.path.join(tmp_dir, 'META-INF/CERT.RSA')
    if os.path.isfile(rsa_file):
      p = subprocess.Popen(
          'keytool -printcert -file %s'
          % pipes.quote(rsa_file), shell=True,
          stdout=subprocess.PIPE)
      md5 = None
      sha1 = None
      sha256 = None
      for line in p.stdout.read().split('\n'):
        m = re.match('MD5:\s+([0-9A-F:]+)', line.strip())
        if m:
          md5 = m.group(1)
        m = re.match('SHA1:\s+([0-9A-F:]+)', line.strip())
        if m:
          sha1 = m.group(1)
        m = re.match('SHA256:\s+([0-9A-F:]+)', line.strip())
        if m:
          sha256 = m.group(1)
      if not md5 or not sha1:
        print prefix + '  *** could not determine md5 and sha1 from cert'
      else:
        # md5
        md5Emoji = ':'.join(HexToEmoji(md5.split(':')))
        print prefix + '  md5: %s' % (md5)
        print prefix + '       %s' % (md5Emoji)
        # sha1
        sha1Emoji = ':'.join(HexToEmoji(sha1.split(':')))
        print prefix + '  sha1: %s' % (sha1)
        print prefix + '        %s' % (sha1Emoji)
        # sha256
        sha256Emoji = ':'.join(HexToEmoji(sha256.split(':')))
        print prefix + '  sha256: %s' % (sha256)
        print prefix + '          %s' % (sha256Emoji)
      if p.wait():
        Fail('keytool failed')
    else:
      print prefix + '  *** no cert file found'
    p = subprocess.Popen('find %s -name "*.apk"' % pipes.quote(tmp_dir),
                         stdout=subprocess.PIPE, shell=True)
    child_apks = [ f for f in p.stdout.read().strip().split('\n') if f ]
    if p.wait():
      Fail('Failed to find apks within parent package')
    for child_apk in child_apks:
      child_apk_rel_path = os.path.relpath(child_apk, tmp_dir)
      AnalyzeApk(child_apk, apk_rel_path=child_apk_rel_path, prefix=prefix+'  ')
  finally:
    shutil.rmtree(tmp_dir)


def HexToEmoji(hexList):
  try:
    import emojiencoder
    indexList = [int(h, 16) for h in hexList]
    return emojiencoder.emojiEncode(indexList)
  except ImportError as error:
    print 'emojiencoder.py not found in this directory'
  return []


if len(sys.argv) < 2:
  Usage()

for apk_path in sys.argv[1:]:
  if not apk_path.endswith('.apk'):
    Usage()

for apk_path in sys.argv[1:]:
  AnalyzeApk(apk_path)
