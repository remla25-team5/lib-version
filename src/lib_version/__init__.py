from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("lib-version")
except PackageNotFoundError:
    pass