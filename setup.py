#!/usr/bin/env python

import os
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup  # type: ignore

# Package meta-data
NAME = "lazydocs"
MAIN_PACKAGE = "lazydocs"  # Change if main package != NAME
DESCRIPTION = "Generate markdown API documentation for Google-style Python docstring."
URL = "https://github.com/ml-tooling/lazydocs"
EMAIL = "team@mltooling.org"
AUTHOR = "ML Tooling Team"
LICENSE = "MIT"
REQUIRES_PYTHON = ">=3.6"
VERSION = None  # Only set version if you like to overwrite the version in _about.py

# Please define the requirements within the requirements.txt

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except maybe the trove classifiers!

PWD = os.path.abspath(os.path.dirname(__file__))


def load_requirements(path_dir=PWD, file_name="requirements.txt", comment_char="#"):
    """Read requirements file and return packages and git repos separately."""
    requirements = []
    dependency_links = []
    with open(os.path.join(path_dir, file_name), "r", encoding="utf-8") as file:
        lines = [ln.strip() for ln in file.readlines()]
    for ln in lines:
        if not ln:
            continue
        if comment_char in ln:
            ln = ln[: ln.index(comment_char)].strip()
        if ln.startswith("git+"):
            dependency_links.append(ln.replace("git+", ""))
        else:
            requirements.append(ln)
    return requirements, dependency_links


# Read the requirements.txt and use it for the setup.py requirements
requirements, dependency_links = load_requirements()
if dependency_links:
    print(
        "Cannot install some dependencies. "
        "Dependency links are currently not supported: " + str(dependency_links)
    )
dev_requirements, _ = load_requirements(file_name="requirements-dev.txt")

# Import the README and use it as the long-description.
with open(os.path.join(PWD, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Load the package's _about.py module as a dictionary.
about = {}  # type: dict
if not VERSION:
    with open(os.path.join(PWD, os.path.join("src", MAIN_PACKAGE), "_about.py")) as f:  # type: ignore
        # todo: extract version via regex? re.findall("__version__ = '([\d.\w]+)'", f.read())[0]
        exec(f.read(), about)
        VERSION = about["__version__"]

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license=LICENSE,
    packages=find_packages(where="src", exclude=("tests", "test")),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    zip_safe=False,
    install_requires=requirements,
    extras_require={
        # extras can be installed via: pip install package[dev]
        "dev": [dev_requirements],
        "test": [dev_requirements],
    },
    include_package_data=True,
    package_data={
        # If there are data files included in your packages that need to be
        # 'sample': ['package_data.dat'],
    },
    # deprecated: dependency_links=dependency_links,
    classifiers=[
        # TODO: Update via https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Changelog": URL + "/releases",
        "Issue Tracker": URL + "/issues",
        "Documentation": URL + "#documentation",
        "Source": URL,
    },
    entry_points={
        "console_scripts": [f"{NAME}={MAIN_PACKAGE}._cli:app"],
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
)
