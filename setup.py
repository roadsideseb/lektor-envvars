import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

requires = ["lektor", "environs"]
tests_requires = ["pytest", "pytest-cache", "pytest-cov"]
lint_requires = ["flake8", "black"]
dev_requires = requires + tests_requires + lint_requires


setup(
    name="lektor-envvars",
    version="18.6.12.1",
    description="A Lektor plugin making environment variables available in templates.",
    long_description="\n\n".join([open("README.rst").read()]),
    license="MIT",
    author="Sebastian Vetter",
    author_email="seb@roadsi.de",
    url="https://www.github.com/elbaschid/lektor-envvars",
    packages=find_packages(),
    install_requires=requires,
    entry_points={"lektor.plugins": ["lektor-envvars = lektor_envvars:EnvvarsPlugin"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    extras_require={"test": tests_requires, "dev": dev_requires, "lint": lint_requires},
)
