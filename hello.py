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
    def firstprint(self, word_to_print):
        """
        """
        def __init__(self, word_to_print):
            self.word_to_print = word_to_print

        def __str__(self):
            return self.__str__()

        log.debug('Logging that word: %s will be printed' % (word_to_print))
        print ('%s' % (word_to_print))

if __name__ == '__main__':
    firstclassmodule = HelloWorld()
    firstclassmodule.firstprint('Hello')
