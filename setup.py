#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


try:
    fh = codecs.open("README.md", encoding="utf-8")
    long_description = fh.read()
    fh.close()
except FileNotFoundError:
    long_description = ""

setup(
        name="pipgui",
        version=1.1,
        description="This package is GUI based tool for installing pip packages in your environment.",
        url="https://github.com/GDGVIT/pip-gui",
        author="Ayush Priya, DSC-VIT",
        author_email="ayushpriya10@gmail.com, dscvitvellore@gmail.com",
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
