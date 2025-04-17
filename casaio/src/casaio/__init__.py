from importlib.metadata import version

__version__ = version("casaio")

from . import io
from . import tablestream