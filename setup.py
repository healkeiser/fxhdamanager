"""PyPI setup script."""

# Built-in
from setuptools import setup, find_packages
from pathlib import Path

# Metadata
__author__ = "Valentin Beaumont"
__email__ = "valentin.onze@gmail.com"


###### CODE ####################################################################


# Add `README.md` as project long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="fxhdamanager",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Houdini digital asset (HDA) management system through Git.",
    url="https://github.com/healkeiser/fxhdamanager",
    author="Valentin Beaumont",
    author_email="valentin.onze@gmail.com",
    license="MIT",
    keywords="VFX Qt Houdini HDA PySide2 DCC UI",
    packages=find_packages(),
    install_requires=[
        "GitPython",
    ],
    include_package_data=True,
)

# To install as a local editable package:
# python -m pip install -e .
