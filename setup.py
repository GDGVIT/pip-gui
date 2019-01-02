import os
import re
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def find_version(*file_paths):
    try:
        f = codecs.open(os.path.join(here, *file_paths), "r", "latin1")
        version_file = f.read()
        f.close()
    except:
        raise RuntimeError("Unable to find version string.")

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


try:
    f = codecs.open("README.rst", encoding="utf-8")
    long_description = f.read()
    f.close()
except:
    long_description = ""

setup(
    name="pipgui",
    version=find_version("pip_gui/mainGUI.py"),
    description="",
    url="https://github.com/GDGVIT/pip-gui",
    author="GDGVIT",
    packages=find_packages(include=[
        "pip_gui",
        "pip_gui.*"
    ]),
    include_package_data=True,
    # py_modules=["pip_gui.mainGUI"],
    entry_points={
        "console_scripts": [
            "pipgui=pip_gui.mainGUI:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: X11 Applications :: Qt",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    install_requires=[
    # "beautifulsoup4>=4.5, <4.5.4"
    "beautifulsoup4"
    ]
)
