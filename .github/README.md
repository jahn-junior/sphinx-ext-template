# Canonical Sphinx extension template

This repository is a template for Canonical's Sphinx extensions. It provides useful
boilerplate and tools for linting, testing, and publishing Sphinx extensions.

## Create a new extension

When creating a new Sphinx extension, [use this
template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
to create your repository.

Once the repository has been created, begin by updating the top-level README and
CONTRIBUTING templates.

Next, replace any references to the placeholder extension, `hello_ext`, in the following
files:

- `pyproject.toml`
- `Makefile`
- `hello_ext/`
- `tests/unit/`
- `tests/integration/`

Finally, delete `.github/README.MD`, as it will take precedence over your top-level
README if left intact.

## Migrate an existing extension

Due to the limited size of most extensions, the easiest way to migrate the code is by
transplanting it into a new repository created from this template. Before moving
forward, follow the steps above to create this new repository.

If the extension previously used a build tool other than uv, you'll need to add any
dependencies to `pyproject.toml` by running `uv add <package-name>` in the project's
root directory.

Next, you'll need to make the code comply with the template's linters. Start by
running:

```bash
make lint
```

This process can be made easier by configuring your preferred text editor to highlight
ruff, pyright, and mypy errors.

Lastly, all extensions expected to be well-tested. Once you have either migrated
existing tests or written new ones, they can be run with:

```bash
make test
```

You can also generate a code coverage report with:

```bash
make test-coverage
```

Once everything passes, the extension's migration is complete.

## License and copyright

This template is released under the [GPL-3.0 license](LICENSE).

© 2025 Canonical Ltd.
