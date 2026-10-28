# qmss-pkgs-cookiecutter

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating a Python package managed with [uv](https://docs.astral.sh/uv/), used in QMSS G5072 *Modern Data Structures* at Columbia University.

It is a fork of [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter) by Tomas Beuzen and Tiffany Timbers, the template that accompanies the [*Python Packages*](https://py-pkgs.org) book. The project layout is the same; Poetry has been replaced with uv throughout.

## Usage

With [uv installed](https://docs.astral.sh/uv/getting-started/installation/), run:

```bash
uvx cookiecutter gh:QMSS-G5072-2026/qmss-pkgs-cookiecutter
```

`uvx` runs Cookiecutter in a temporary environment, so nothing needs to be installed first. Answer the prompts, then:

```bash
cd mypkg
uv sync          # creates .venv, installs your package and its dev/docs groups, writes uv.lock
uv run pytest    # runs the (empty) test suite
```

## What you get

```
mypkg
├── .github/workflows        ← GitHub Actions: tests and docs on every push (optional: publish on tags)
├── .readthedocs.yml         ← Read the Docs configuration (installs with uv)
├── .python-version          ← Python version uv uses for development
├── CHANGELOG.md
├── CONDUCT.md
├── CONTRIBUTING.md
├── docs                     ← Sphinx documentation (MyST Markdown + notebooks, AutoAPI)
├── LICENSE
├── pyproject.toml           ← project metadata, dependency groups, uv_build backend
├── README.md
├── src
│   └── mypkg
│       ├── __init__.py
│       └── mypkg.py
└── tests
    └── test_mypkg.py
```

## Prompts

| Prompt | Default | Notes |
|---|---|---|
| `author_name` | Monty Python | |
| `author_email` | monty@example.com | |
| `package_name` | mypkg | Lowercased; spaces and dashes become underscores |
| `package_short_description` | A package for doing great things! | |
| `package_version` | 0.1.0 | |
| `python_version` | 3.13 | Minimum supported Python (`requires-python`) |
| `open_source_license` | MIT | Written to `pyproject.toml` as an SPDX expression |
| `include_github_actions` | ci | `ci`: tests + docs; `ci+cd`: also publishes to TestPyPI when you push a `v*` tag; `no` |

## Testing the template

```bash
uv run --no-project --with cookiecutter --with pytest pytest tests/
```
