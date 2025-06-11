import shutil
import subprocess
from pathlib import Path

import bs4
import pytest


@pytest.fixture
def example_project(request) -> Path:
    project_root = request.config.rootpath
    example_dir = project_root / "tests/integration/example"

    target_dir = Path().resolve() / "example"
    shutil.copytree(example_dir, target_dir)

    return target_dir


@pytest.mark.slow
def test_hello_integration(example_project):
    build_dir = example_project / "_build"
    subprocess.check_call(
        ["sphinx-build", "-b", "html", "-W", example_project, build_dir],
    )

    index = build_dir / "index.html"
    soup = bs4.BeautifulSoup(index.read_text(), features="lxml")
    shutil.rmtree(example_project)

    ext_text = soup.find("p")
    if ext_text:
        assert getattr(ext_text, "text", None) == "Hello, world!"
    else:
        pytest.fail("Directive output not found in document.")
