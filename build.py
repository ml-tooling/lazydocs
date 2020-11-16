import argparse
import os
import re
import sys
from shutil import rmtree
from typing import Dict, Union

from universal_build import build_utils

MAIN_PACKAGE = "lazydocs"
GITHUB_URL = "https://github.com/ml-tooling/lazydocs"

HERE = os.path.abspath(os.path.dirname(__file__))


def main(args: Dict[str, Union[bool, str]]):

    # set current path as working dir
    os.chdir(HERE)

    version = args[build_utils.FLAG_VERSION]

    if version:
        # Replace version in about.py
        with open(os.path.join(HERE, f"src/{MAIN_PACKAGE}/_about.py"), "r+") as f:
            data = f.read()
            f.seek(0)
            f.write(re.sub(r"__version__ = \".+\"", f'__version__ = "{version}"', data))
            f.truncate()

    if args[build_utils.FLAG_CHECK]:
        _check(args)

    if args[build_utils.FLAG_MAKE]:
        _make(args)

    if args[build_utils.FLAG_TEST]:
        _test(args)

    if args[build_utils.FLAG_RELEASE]:
        _release(args)


def _check(args: Dict[str, Union[bool, str]]):
    """Run linting and style checks via black, isort, mypy and flake8."""
    build_utils.run("pip install -e .[dev]", exit_on_error=True)
    # Run linters and checks
    build_utils.run("black --check src", exit_on_error=True)
    build_utils.run("black --check tests", exit_on_error=True)
    build_utils.run("isort --profile black --check-only src", exit_on_error=True)
    build_utils.run("isort --profile black --check-only tests", exit_on_error=True)
    build_utils.run("mypy src", exit_on_error=True)
    build_utils.run("flake8 --show-source --statistics src", exit_on_error=True)
    build_utils.run("flake8 --show-source --statistics tests", exit_on_error=True)
    build_utils.run("pydocstyle src", exit_on_error=True)


def _make(args: Dict[str, Union[bool, str]]):
    """Build the library."""

    try:
        # Ensure there are no old builds
        rmtree(os.path.join(HERE, "dist"))
    except OSError:
        pass

    # Build the distribution archives
    build_utils.run(
        f"{sys.executable} setup.py sdist bdist_wheel clean --all",
        exit_on_error=True,
    )

    # Check the archives with twine
    build_utils.run("twine check dist/*", exit_on_error=True)

    # Install library
    build_utils.run("pip install -e .[dev]", exit_on_error=True)
    # Create API documentation via lazydocs
    build_utils.run(
        f"lazydocs --overview-file=README.md --src-base-url={GITHUB_URL}/blob/main {MAIN_PACKAGE}",
        exit_on_error=True,
    )


def _test(args: Dict[str, Union[bool, str]]):
    """Run all tests."""
    # Install library
    build_utils.run("pip install -e .[dev]", exit_on_error=True)
    # Execute tests with coverage check
    # build_utils.run(
    #     f"pytest --cov={MAIN_PACKAGE} --cov-report=xml --cov-report term --cov-report=html tests",
    #     exit_on_error=True,
    # )


def _release(args: Dict[str, Union[bool, str]]):
    """Publish library to pypi repository."""
    pypi_user = "__token__"
    pypi_repository_args = ""  # Use main repository

    if "pypi_token" in args:
        pypi_token = args["pypi_token"]
    else:
        build_utils.log("PyPI token is required for release (--pypi-token=<TOKEN>)")
        build_utils.exit_process(1)

    if "pypi_repository" in args and args["pypi_repository"]:
        pypi_repository_args = '--repository-url "' + str(args["pypi_repository"]) + '"'

    # Publish on pypi
    build_utils.run(
        f'twine upload --non-interactive -u "{pypi_user}" -p "{pypi_token}" {pypi_repository_args} dist/*',
        exit_on_error=True,
    )

    # Publish coverage report: if private repo set CODECOV_TOKEN="token" or use -t
    build_utils.run("curl -s https://codecov.io/bash | bash -s", exit_on_error=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pypi-token", help="Personal access token for PyPI account.", required=False
    )
    parser.add_argument(
        "--pypi-repository",
        help="PyPI repository for publishing artifacts.",
        required=False,
    )

    args = build_utils.get_sanitized_arguments(argument_parser=parser)
    main(args)
