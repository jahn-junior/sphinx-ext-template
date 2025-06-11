import pathlib
import sys

project_dir = pathlib.Path(__file__).parents[1].resolve()
sys.path.insert(0, str(project_dir.absolute()))

project = "Mockumentation"
author = "Tester"

html_title = project

extensions = [
    "hello_ext",
]
