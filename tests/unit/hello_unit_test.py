import pytest
from docutils.core import publish_doctree
from hello_ext.hello import HelloDirective
from typing_extensions import override


class FakeHelloDirective(HelloDirective):
    @override
    def __init__(self, arguments):
        self.arguments = arguments


@pytest.fixture
def fake_hello_directive(request: pytest.FixtureRequest) -> FakeHelloDirective:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeHelloDirective(arguments=overrides.get("arguments", []))


@pytest.mark.parametrize(
    "fake_hello_directive",
    [{"arguments": ["world"]}],
    indirect=True,
)
def test_hello_directive(fake_hello_directive: FakeHelloDirective):
    expected = publish_doctree("Hello, world!").children
    actual = fake_hello_directive.run()

    assert str(expected) == str(actual)
