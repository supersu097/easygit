#!/usr/bin/env python3
# coding=utf-8

import os


def gitpush():
    i = 1
    filelist = os.listdir("./")
    for currentfile in filelist:
        print(str(i) + ". " + str(currentfile))
        i += 1
    filename = input("Please choose what you wanna to push(default is all): ")
    if filename == "":
        os.system("git add ./")
    else:
        try:
            choosenumber = int(filename)
            if choosenumber <= len(filelist):
                os.system("git add " + filelist[choosenumber-1])
            else:
                print("The number you input is too large,Please retry it!")
                exit()
        except ValueError as e:
            print("ErrorOccur: " + str(e))
            exit()

    commitmessage = input("Please input the commit message(default is nothing to record): ")
    if commitmessage == "":
        os.system("git commit -m 'change a lot,nothing wanna fucking record'")
    else:
        os.system("""git commit -m "%s" """ % commitmessage)

    os.system("git push origin master")

gitpush()

