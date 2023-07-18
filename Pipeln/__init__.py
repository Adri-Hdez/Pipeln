# Custom Pipeline Creator (Pipeln)
#
# Authors: Adrián Hernández S. <adrihs.dev@gmail.com>
# For license information, see LICENSE

import os
from .pipeline import Pipeline

# //////////////////////////////////////////////////////
# Metadata
# //////////////////////////////////////////////////////

# Version.  For each new release, the version number should be updated
# in the file VERSION.
try:
    # If a VERSION file exists, use it!
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    with open(version_file) as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = "unknown (running code interactively?)"
except OSError as ex:
    __version__ = "unknown (%s)" % ex

__license__ = 'MIT License'

# Maintainer, contributors, etc.
__maintainer__ = 'Adrián Hernández S.'
__maintainer_email__ = 'adrihs.dev@gmail.com'
__author__ = __maintainer__
__author_email__ = __maintainer_email__

__all__ = [
    "__version__",
    "Pipeline"
]