import argparse
import sys
from pathlib import Path


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        """
        Method modifies default errors from argparse.ArgumentParser class.
        Prints a usage message incorporating the message to stderr and exits.
        """
        self.print_help(sys.stderr)
        self.exit(2, 'Something went wrong - > %s\nPlease, check the "help" and try again\n' % message)

    def valid_path(self, path):
        """
        Method checks if passed into function path exists and tries to create it if it doesn't.
        If path exists  or is created successfully, method returns given path,
        else - returns default path value for saving files.
        :param path: path to check
        :return: path for saving files
        """
        p = Path(path)
        default = Path.cwd() / "default_dir"
        if p.exists():
            return p
        else:
            self.valid_path(p.parent)
            try:
                if p.suffix == ".pdf":
                    with open(p, "wb"):
                        pass
                elif p.suffix == ".html":
                    with open(p, "w"):
                        pass
                else:
                    if not p.is_dir():
                        p.mkdir()
            except OSError:
                print("Invalid path.. Saving to the project default dir")
                if not default.is_dir():
                    default.mkdir()
                return default
            else:
                return p
