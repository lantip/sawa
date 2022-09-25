#!/usr/bin/env python3
'''
ꦱꦮ is an open source programming language, an interpreter to be precise, where you can write Python code using Javanese character.
https://github.com/lantip/sawa/docs/
Licensed under ABRMS License
Copyright (c) 2021 ꦱꦮ  
'''
import sys
import os
import argparse
import sawa.main as mn
from subprocess import call

def error(_error, message):
    """ Print errors to stdout
    """
    print("[-] {}: {}".format(_error, message))
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='ꦒꦩ꧀ꦧꦂꦥ꦳ꦶꦧꦺꦴꦤꦕꦶ')
    parser.add_argument('name', type=str, help='filename with extension .ꦱꦮ')
    args = parser.parse_args()

    if not 'ꦱꦮ' in args.name:
        error("Error",
                  "Please use ꦱꦮ as extension.")
    file_name = args.name.split('.')
    if os.path.isfile(file_name[0]+'.py'):
        os.remove(file_name[0]+'.py') 
    mn.main(args.name)
    call('python3 %s.py' % (file_name[0]), shell=True)
    os.remove(file_name[0]+'.py')

def versionCompare(v1, v2):
    arr1 = v1.split(".")
    arr2 = v2.split(".")
    n = len(arr1)
    m = len(arr2)
    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]
  
    if n>m:
      for i in range(m, n):
         arr2.append(0)
    elif m>n:
      for i in range(n, m):
         arr1.append(0)
     
    for i in range(len(arr1)):
      if arr1[i]>arr2[i]:
         return 1
      elif arr2[i]>arr1[i]:
         return -1
    return 0

def run_as_command():
    version = ".".join(str(v) for v in sys.version_info[:2])
    ans = versionCompare('3.6', version)
    if ans > 0:
        print("[-] ꦱꦮ mbutuhaké Python vèrsi 3.6 munggah.")
        sys.exit(0)

    main()


if __name__ == '__main__':
    main()
