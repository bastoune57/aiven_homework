import setuptools
from os import path

DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

# read Readme file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# read licese file for licensing info
with open('LICENSE') as f:
    license = f.read()

# setup package informations
setuptools.setup(
    name="homework-pkg-bastoune57",
    version="0.0.1",
    author="Bastien Hamet",
    author_email="bastien.hamet@gmail.com",
    description="Package made with the code for the Aiven homework",
    install_requires=INSTALL_PACKAGES,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bastoune57/aiven_homework",
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    license=license,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
