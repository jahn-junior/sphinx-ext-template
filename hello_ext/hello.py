"""Contains the extension's directive."""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class HelloDirective(SphinxDirective):
    """A directive to say hello."""

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        """Write a greeting.

        :returns: list[nodes.Node]
        """
        paragraph_node = nodes.paragraph(text=f"Hello, {self.arguments[0]}!")
        return [paragraph_node]
