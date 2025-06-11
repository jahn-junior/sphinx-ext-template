"""Adds the directive to Sphinx."""

from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx
from .hello import HelloDirective

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("hello_ext")
    except PackageNotFoundError:
        __version__ = "dev"


def setup(app: Sphinx) -> ExtensionMetadata:
    """Add the extension's directive to Sphinx.

    :returns: ExtensionMetadata
    """
    app.add_directive("hello", HelloDirective)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


__all__ = ["__version__", "setup"]
