#!/usr/bin/env python
import sys
import subprocess
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')


class HelloWorld:
    """
    First class that include some basics like print, logging, warning messages.
    """

    def __init__(self, word_to_print=None):
        self.word_to_print = word_to_print

    def __str__(self):
        return self.word_to_print

    def __repr__(self):
        return self.__str__()

    def firstprint(self, word_to_print=None):
        """
        Module print on screen words that user provide. Next do the shell
        action and write that word to the file i user home catalog.
        """

        log.debug('Logging that word: %s will be printed' % (word_to_print))
        print ('%s' % (word_to_print))

    def writewordtofile(self, word_to_write):
        """
        """

        log.info('Wrting %s word to the file' % (word_to_write))
        writehellotofile = open('/home/aolechno/writehellotofile.txt', 'a')
        writehellotofile.write(r'%s \n' % (word_to_write))
        writehellotofile.close()


class LsShellPrint:
    """
    """

    def __init__(self, pathinshell=None):
        self.pathinshell = pathinshell

    def __str__(self):
        return ('%s' % (self.pathinshell))

    def __repr__(self):
        return self.__str__()

    def printlscmd(self, pathinshell):
        """
        """

        log.info('List files and directores in shell in specified path:'
                 ' %s will be printed' % (pathinshell))
        lsprint = subprocess.Popen(["ls", "-lah", pathinshell], stdin=None,
                                   stdout=None, stderr=None, shell=False)

if __name__ == '__main__':
    firstclassmodule = HelloWorld()
    firstclassmodule.firstprint('Hello')
    firstclassmodule.writewordtofile('Hello')
    firstlistmodule = LsShellPrint()
    firstlistmodule.printlscmd("/home/aolechno")
