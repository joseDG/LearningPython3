

import os

# directories where EXECUTABLE programs are located
print(os.environ.get('PATH'))   # e.g. some <>/bin paths

# Most important for us
print(os.environ.get('PYTHONPATH'))


import sys  # parameters specific to the system

# Search path for modules (coming).
# 1) Script's directory (or current for interactive)
# 2) Initialized from the environment variable PYTHONPATH,
# 3) plus an installation-dependent default.
print(sys.path)

