import {{ cookiecutter.__package_slug }}


def test_version_is_defined():
    assert isinstance({{ cookiecutter.__package_slug }}.__version__, str)
