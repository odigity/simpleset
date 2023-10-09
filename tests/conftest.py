# Reminder:  This module is automatically loaded by pytest in a new process.
#            It will not inherit any sys.path fixes applied to the parent process.
from pathlib import Path
import sys


PACKAGE_ROOT = Path( __file__ ).resolve().parent    # py-objects/tests/
REPO_ROOT    = PACKAGE_ROOT.parent                  # py-objects/

# add REPO_ROOT to path so `objects` package can be imported by tests
sys.path.insert( 0, str( REPO_ROOT ) )
