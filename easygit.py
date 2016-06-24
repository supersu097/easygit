#!/usr/bin/env python
# coding=utf-8

import os
import argparse


def gitpush(filename,allfile):
    if filename:
        os.system("git add %s" % filename)
    elif allfile:
        os.system("git add ./")


    commitmessage = raw_input("Please input the commit message "
                          "(default is nothing to record): ")
    if commitmessage == "":
        os.system("git commit -m 'change a lot,"
                  "nothing wanna fucking record'")
    else:
        os.system("""git commit -m "%s" """ % commitmessage)

    os.system("git push origin master")


if __name__=='__main__':
    parser=argparse.ArgumentParser(
        description='a simple py script to help you use git easily'
    )
    group=parser.add_mutually_exclusive_group(
        required=True
    )
    group.add_argument(
        '-f','--filename',
        help='the file you wanna push to the remote git server',
        type=file
    )
    group.add_argument(
        '-a','--allfile',
        help='add all edited but not staged for commit file',
        action="store_true"
    )
    args=parser.parse_args()
    gitpush(args.filename,args.allfile)

