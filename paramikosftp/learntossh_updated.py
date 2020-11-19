#!/usr/bin/env python3

## std library impports on top
import os
import sys

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue

def opencmdfile(filein):
    
    if filein == ''
    
        infile = input("Enter filename of the commands to be run: ")

        try:
            with open(infile, "r") as cmdfile:
                cmds = cmdfile.read().strip("\n")
        except:
            print(f"{infile} couldn't be opened.")

    else:

        try:
            with open(filein, "r") as cmdfile:
                cmds = cmdfile.read().strip("\n")

        except:
            print(f"{filein} couldn't be opened.")

    return cmds


def gethosts(hostin):
    if hostin == ''

        inhost = input("Enter filename of the commands to be run: ")

        try:
            with open(infile, "r") as cmdfile:
                cmds = cmdfile.read().strip("\n")
        except:
            print(f"{inhost} couldn't be opened.")

    else:

        try:
            with open(hostin, "r") as cmdfile:
                cmds = cmdfile.read().strip("\n")

        except:
            print(f"{hostin} couldn't be opened.")

    return cmds


def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
  
  ## create SSH connection
  sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)
  
  our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
  
  for x in our_commands:
    ## call our imported function and save the value returned
    resp = cmdissue(x, sshsession)
    ## if returned response is not null, print it out
    if resp != "":
      print(resp)
  
  ## end the SSH connection
  sshsession.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Test SSH with file input")
    parser.add_argument('cmdf', metavar='CMDFILE',
                        type=str, default='cmdfile', help="Enter CMD File")
    parser.add_argument('hstf', metavar='HOSTFILE',
                        type=str, default='hostfile', help="Enter CMD File")
    args = parser.parse_args()
  main()


