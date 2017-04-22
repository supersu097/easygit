#!/usr/bin/env python
# coding=utf-8

import argparse
import os
import subprocess
import sys


class Misc():
    GREEN = '\033[32m'
    RED = '\033[31m'
    END = '\033[0m'

    def red_print(self, Uprint):
        print(self.RED + Uprint + self.END)

    def green_print(self, Uprint):
        print(self.GREEN + Uprint + self.END)

    def gitver_show(self):
        self.green_print("Your Git version is shown as below:")
        os.system('git --version')

    def gittree_show(self):
        self.green_print("\nYour working tree status is shown as below:")
        os.system('git status')

    def gitadd_option(self, gitver):
        self.green_print("\nDue to your current Git version\n"
                         "of '{0}',you have these options for"
                         "`git add` shown as below:".format(gitver))

    def choice_check(self):
        while True:
            choice = raw_input('Pls choose which option\n'
                               'of number you wanna run shown as above %s: ' % range(1, 4))
            if choice == '':
                self.green_print("Nothing input,it's default to execute option 1.\n")
                return 1
            try:
                if int(choice) not in range(1, 4):
                    self.red_print('Error: Your choice\n'
                                   'out of range,pls try again!\n')
                    continue
                else:
                    return choice
            except ValueError:
                self.red_print('Error: We need a number,\n'
                               'You input wrong type,just try again!\n')
                continue

    def choice_exe(self, choicenum, gitadd_command):
        self.green_print("You choose No.{0},\n"
                         "so the command of '{1}' will "
                         "be executed right now!\n".format(choicenum, gitadd_command))
        os.system(gitadd_command)
        self.gittree_show()

    def gitcommit_push(self):
        commitmessage = raw_input("Pls input the commit message\n"
                                  "  (default is nothing to commit): ")
        extended_desc = raw_input("Sometimes U'd wanna leave extended description here\n"
                                  "  (Default is leaving blank here): ")
        if commitmessage == "" and extended_desc == "":
            os.system("git commit -m 'no fucking message wanna commit'")

        else:
            os.system("""git commit -m "{0}" -m "{1}" """.format(
                commitmessage, extended_desc))

        curr_branch = subprocess.check_output('git branch',shell=True).split()[1]
        os.system("git push origin {0}".format(curr_branch))
        self.gittree_show()

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
        print('Distinction between several '
              'git-add options:\n' + fyi + '\n')

    def gitrepo_check(self):
        if os.system('git status >/dev/null 2>&1') != 0:
            os.system('git status')
            sys.exit(1)


def main(filename):
    Misc().gitrepo_check()
    if filename:
        if len(filename) == 1:
            os.system("git add " + filename[0].name)
            Misc().gittree_show()
            Misc().gitcommit_push()
        else:
            filelist=[]
            for li in filename:
                filelist.append(li.name)
            os.system("git add " + ' '.join(filelist))
            Misc().gittreeshow()
            Misc().gitcommit_push()

    else:
        gitver = subprocess.check_output(
            ['git', '--version']).split()[2]

        if int(gitver[0]) == 1:
            Misc().gitver_show()
            Misc().gittree_show()
            Misc().gitadd_option(gitver)

            print("1. git add -A ---------> Stage All(new,modified,deleted) file\n"
                  "2. git add .  ---------> Stage New and Modified files only\n"
                  "3. git add -u ---------> Stage Modified and Deleted files only")
            Misc().fyi()
            # For git V1.x,use the default param
            Misc().choice_match()
            Misc().gitcommit_push()

        elif int(gitver[0]) == 2:
            Misc().gitver_show()
            Misc().gittree_show()
            Misc().gitadd_option(gitver)

            print("1. git add -A = git add . -----> Stage All(new,modified,deleted) file\n"
                  "2. git add -ignore-removal ----> Stage New and Modified files only\n"
                  "3. git add -u -----------------> Stage Modified and Deleted files only\n")

            Misc().fyi()
            # For git V2.x,use the special param
            Misc().choice_match('-ignore-removal')
            Misc().gitcommit_push()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='a simple py script to help me use git easily',
        epilog='Note that: Without any arg passed is mean to '
               'execute the ordinary git flow command then just '
               'flow the prompt')

    parser.add_argument(
        '-f', '--filename',
        help='the file you wanna push to the remote git server,\n'
             'support multiple filename as args',
        type=file,
        nargs='*')

    args = parser.parse_args()
    main(args.filename)
