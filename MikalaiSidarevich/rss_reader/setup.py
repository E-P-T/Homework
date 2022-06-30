"""
Install required packages for RSS reader.
"""

import os
import sys

cmd = f"{sys.executable} -m pip install -r requirements.txt"
os.system(cmd)
