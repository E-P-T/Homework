"""
__main__.py module makes it possible to run application as module like this: rss_reader
"""

from rss_reader import read_defs
import sys
from pathlib import Path

# add rss_reader package path to sys.path
rss_reader_pkg_dir_path = str(Path(__file__).parent.resolve())
sys.path.insert(1, rss_reader_pkg_dir_path)


if __name__ == "__main__":
    read_defs()
