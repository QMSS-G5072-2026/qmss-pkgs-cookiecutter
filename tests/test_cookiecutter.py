import json
import subprocess
import tomllib
from itertools import product
from pathlib import Path

from pytest import fixture, mark

IGNORE = [".DS_Store", "__pycache__"]

with open("cookiecutter.json") as f:
    options = json.load(f)
combinations = list(
    product(options["open_source_license"], options["include_github_actions"])
)


@fixture()
def output_dir(tmp_path):
    return tmp_path


def bake(output_dir, **params):
    extra = " ".join(f'{key}="{value}"' for key, value in params.items())
    command = f"cookiecutter . --no-input --output-dir {output_dir} {extra}"
    return subprocess.run(command, shell=True)


def num_items(path):
    return len([item for item in path.iterdir() if item.name not in IGNORE])


def test_cookiecutter_default_options(output_dir):
    assert bake(output_dir).returncode == 0
    pyproject = tomllib.loads((output_dir / "mypkg" / "pyproject.toml").read_text())
    assert pyproject["project"]["license"] == "MIT"
    assert pyproject["project"]["requires-python"] == ">=3.13"
    assert pyproject["build-system"]["build-backend"] == "uv_build"


@mark.parametrize("open_source_license,include_github_actions", combinations)
def test_cookiecutter_all_options(output_dir, open_source_license, include_github_actions):
    result = bake(
        output_dir,
        open_source_license=open_source_license,
        include_github_actions=include_github_actions,
    )
    assert result.returncode == 0

    path = output_dir / "mypkg"
    assert num_items(path / "tests") == 1
    assert num_items(path / "src" / "mypkg") == 2
    assert num_items(path / "docs") == 8

    pyproject = tomllib.loads((path / "pyproject.toml").read_text())
    has_license = open_source_license != "None"
    assert ("license" in pyproject["project"]) == has_license
    assert (path / "LICENSE").exists() == has_license

    has_actions = include_github_actions != "no"
    assert (path / ".github").exists() == has_actions
    if has_actions:
        assert num_items(path / ".github" / "workflows") == 1

    # .github, .gitignore, .python-version, .readthedocs.yml, CHANGELOG, CONDUCT,
    # CONTRIBUTING, docs, LICENSE, pyproject.toml, README, src, tests
    assert num_items(path) == 11 + has_license + has_actions
