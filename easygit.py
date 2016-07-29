#!/usr/bin/env python
# coding=utf-8

import os
import argparse
import subprocess


class Misc():
    GREEN = '\033[32m'
    RED = '\033[31m'
    END = '\033[0m'

    def redprint(self, Uprint):
        print(self.RED + Uprint + self.END)

    def greenprint(self, Uprint):
        print(self.GREEN + Uprint + self.END)

    def gitverShow(self):
        self.greenprint("Your Git version is shown as below:")
        os.system('git --version')

    def gittreeShow(self):
        self.greenprint("\nYour working tree status is shown as below:")
        os.system('git status')

    def gitinit(self):
        self.gitverShow()
        self.gittreeShow()

    def gitaddOption(self, gitver):
        Misc().greenprint("\nDue to your current Git version\n"
                          "of '{0}',you have these options for"
                          "`git add` shown as below:".format(gitver))

    def choice_check(self):
        while True:
            choice = raw_input('Pls choose which action\n'
                               'of number you wanna do shown as above [1,2,3]: ')

            try:
                if int(choice) not in [1, 2, 3]:
                    self.redprint('Error: Your choice\n'
                                  'out of range,pls try again!\n')
                    continue
                else:
                    return choice
            except ValueError:
                self.redprint('Error: We need a number,\n'
                              'You input wrong type,just try again!\n')
                continue

    def choice_exe(self, choicenum, command):
        self.greenprint("You choose No.{0},\n"
                        "so the command of '{1}' will "
                        "be execute right now!\n".format(choicenum, command))
        os.system(command)
        self.greenprint('Now your working tree status is shown as below:')
        os.system('git status')

    def gitcommit_push(self):
        commitmessage = raw_input("Please input the commit message\n"
                                  "  (default is nothing to record): ")
        if commitmessage == "":
            os.system("git commit -m 'change a lot,"
                      "nothing wanna fucking record'")
        else:
            os.system("git commit -m '%s'" % commitmessage)
            os.system("git push origin master")

    def choice_match(self, specialcase='.'):
        choice = self.choice_check()
        if int(choice) == 1:
            Misc().choice_exe(1, 'git add -A')

        elif int(choice) == 2:
            Misc().choice_exe(2, 'git add %s' % specialcase)

        elif int(choice) == 3:
            Misc().choice_exe(3, 'git add -u')

    def fyi(self):
        fyi = 'http://stackoverflow.com/questions/572549/'
        print('FYI of difference between kinds of '
              'git add options:\n' + fyi + '\n')


def main(filename, add_option):
    if filename:
        if len(filename) == 1:
            os.system("git add " + filename)
        else:
            os.system("git add " + ' '.join(filename))

    elif add_option:
        gitver = subprocess.check_output(
            ['git', '--version']).split()[2]

        if int(gitver[0]) == 1:
            Misc().gitinit()
            Misc().gitaddOption(gitver)

            print("1. git add -A ---------> Stage All(new,modified,deleted) file\n"
                  "2. git add .  ---------> Stage New and Modified files only\n"
                  "3. git add -u ---------> Stage Modified and Deleted files only")
            Misc().fyi()
            Misc().choice_match()
            Misc().gitcommit_push()

        elif int(gitver[0]) == 2:
            Misc().gitinit()
            Misc().gitaddOption(gitver)

            print("1. git add -A = git add . -----> Stage All(new,modified,deleted) file\n"
                  "2. git add -ignore-removal ----> Stage New and Modified files only\n"
                  "3. git add -u -----------------> Stage Modified and Deleted files only\n")

            Misc().fyi()
            Misc().choice_match('-ignore-removal')
            Misc().gitcommit_push()


def othercase(oc):
    if oc:
        Misc().gittreeShow()
        Misc().gitcommit_push()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='a simple py script to help you use git easily')

    group = parser.add_mutually_exclusive_group()
        #required=True)

    group.add_argument(
        '-f', '--filename',
        help='the file you wanna push to the remote git server,\n'
             'support multiple filename as args',
        type=file,
        nargs='*')

    group.add_argument(
        '-a', '--add_option',
        help='add one or more case of file changes between new,\n'
             'modified and deleted to stage regarding your local\n'
             'git version and your choice',
        action="store_true")

    parser.add_argument(
        '-o', '--other_case',
        help='other case of change except for new,modified\n'
             'and deleted,then just commit and push',
        action='store_true')

    args = parser.parse_args()
    othercase(args.other_case)
    main(args.filename, args.add_option)
