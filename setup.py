#!/usr/bin/env python3
from setuptools import find_namespace_packages
from setuptools import setup

from utilsfolder import version as deb_ver

PACKAGES = find_namespace_packages(exclude=["tests", "tests.*"])
PROJECT_PACKAGE_NAME = "magic_number"
PROJECT_AUTHOR = "Adrian Ivanescu"
PROJECT_EMAIL = "adrian.ivanescu@outlook.com"
GITHUB_URL = "https://github.com/"
GITHUB_USER = "AdrianIvanescu"
GITHUB_REPOSITORY = "rando"
GITHUB_PATH = "/".join([GITHUB_USER, GITHUB_REPOSITORY])
PROJECT_URL = "/".join([GITHUB_URL, GITHUB_PATH])
MIN_PY_VERSION = ">=3.7"
REQUIRES = [
    "colorama>=0.4.4",
]
setup(
    name=PROJECT_PACKAGE_NAME,
    version=deb_ver.__version__,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    packages=PACKAGES,
    python_requires=MIN_PY_VERSION,
    install_requires=REQUIRES,
    entry_points={
        "console_scripts": ["magic=magic_number:main"]
    },
)
