#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def find_version(*file_paths):
    try:
        fh = codecs.open(os.path.join(here, *file_paths), "r", "latin1")
        version_file = fh.read()
        fh.close()
    except FileNotFoundError:
        raise RuntimeError("Unable to find version string.")

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


try:
    fh = codecs.open("README.md", encoding="utf-8")
    long_description = fh.read()
    fh.close()
except FileNotFoundError:
    long_description = ""

setup(
        name="pipgui",
        version=find_version("pipgui/mainGUI.py"),
        description="This package is GUI based tool for installing pip packages in your environment.",
        url="https://github.com/GDGVIT/pip-gui",
        author="Ayush Priya",
        packages=find_packages(include=[
            "pipgui",
            "pipgui.*"
        ]), 
        include_package_data=True,
        # py_modules=["pip_gui.mainGUI"],
        entry_points={
            "console_scripts": [
                "pipgui=pipgui.mainGUI:main"
            ]
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Environment :: X11 Applications :: Qt",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
        install_requires=[
            "PyQt5",
            "beautifulsoup4"
        ]
)
