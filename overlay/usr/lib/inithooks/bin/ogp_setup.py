#!/usr/bin/python
# Copyright (c) 2008 Alon Swartz <alon@turnkeylinux.org> - all rights reserved

"""
Preinstall openGameManager Games

Options:
    -g --game=    (optional) Pass in a game to install

"""

import re
import sys
import time
import getopt

import signal

from dialog_wrapper import Dialog
from executil import ExecError, system

DEBIAN_CNF = "/etc/mysql/debian.cnf"

class Error(Exception):
    pass

def escape_chars(s):
    """escape special characters: required by nested quotes in query"""
    s = s.replace("\\", "\\\\")  # \  ->  \\
    s = s.replace('"', '\\"')    # "  ->  \"
    s = s.replace("'", "'\\''")  # '  ->  '\''
    return s

#class MySQL:
#    def __init__(self):
#        system("mkdir -p /var/run/mysqld")
#        system("chown mysql:root /var/run/mysqld")
#
#        self.selfstarted = False
#        if not self._is_alive():
#            self._start()
#            self.selfstarted = True
#
#    def _is_alive(self):
#        try:
#            system('mysqladmin -s ping >/dev/null 2>&1')
#        except ExecError:
#            return False
#
#        return True
#
#    def _start(self):
#        system("mysqld --skip-networking >/dev/null 2>&1 &")
#        for i in range(6):
#            if self._is_alive():
#                return
#
#            time.sleep(1)
#
#        raise Error("could not start mysqld")
#
#    def _stop(self):
#        if self.selfstarted:
#            system("mysqladmin --defaults-file=%s shutdown" % DEBIAN_CNF)
#
#    def __del__(self):
#        self._stop()
#
#    def execute(self, query):
#        system("mysql --defaults-file=%s -B -e '%s'" % (DEBIAN_CNF, query))

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "hu:p:",
                     ['help', 'game='])

    except getopt.GetoptError, e:
        usage(e)

#    username="root"
#    password=""
#    queries=[]

    game_install = ""

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-g', '--game'):
            game_install = val

##    if not password:

    d = Dialog('TurnKey Linux - First boot configuration')
    choices = [
                ('Done','Continue Setup'),
                ('L4D2','Install L4D2')
               ]



    while True:
      if not game_install:
         game_install = d.menu(
               "Game Install Menu",
               "Which games would you like to pre-install?",
               choices)

      if game_install == "Done":
        break

      if game_install == "L4D2":
        system("touch /tmp/l4d2")
        game_install = ""

    #    password = d.get_password(
    #        "MySQL Password",
    #        "Please enter new password for the MySQL '%s' account." % username)

    

##    m = MySQL()

    # set password
##    m.execute('update mysql.user set Password=PASSWORD(\"%s\") where User=\"%s\"; flush privileges;' % (escape_chars(password), username))

    # edge case: update DEBIAN_CNF
##    if username == "debian-sys-maint":
##        old = file(DEBIAN_CNF).read()
##        new = re.sub("password = (.*)\n", "password = %s\n" % password, old)
##        file(DEBIAN_CNF, "w").write(new)

    # execute any adhoc specified queries
##    for query in queries:
##        m.execute(query)

if __name__ == "__main__":
    main()

