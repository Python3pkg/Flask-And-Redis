"""
==============
testapp.compat
==============

Additional compatibility helpers to work on both of Python 3 and 2.

"""

from flask_redis import IS_PY3


iteritems = lambda data: list(data.items()) if IS_PY3 else iter(data.items())
iterkeys = lambda data: list(data.keys()) if IS_PY3 else iter(data.keys())
