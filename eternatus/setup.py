import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="x5",
    version="1.0.0",
    description="x5 NexT Gen Project Manager",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ardustri/Externatus/eternatus",
    author="Ardustri",
    author_email="info@externatus.com",
    license="GPL3",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["x5"],
    include_package_data=True,
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "x5=__main__:main",
        ]
    },
)