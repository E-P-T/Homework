import argparse
import sys


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, 'Something went wrong - > %s\nPlease, check the "help" and try again\n' % message)

