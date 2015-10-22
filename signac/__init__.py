"""
signac aids in the management, access and analysis of large-scale
computational investigations.

The framework provides a simple data model, which helps to organize
data production and post-processing as well as distribution among collaboratos.
"""

# The VERSION string represents the actual (development) version of the
# package.
VERSION = '0.1.7'
# The VERSION_TUPLE is used to identify whether signac projects, are
# required to be updated and can therefore lag behind the actual version.
VERSION_TUPLE = 0, 1, 7

from . import contrib
from .common.host import get_db

__all__ = [contrib, get_db]