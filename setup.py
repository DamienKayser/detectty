#!/usr/bin/env python

import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="detectty",
    version="1.3.0",
    author="Daniel Keller",
    author_email="develop@dkkeller.de",
    description="Detects freshly plugged serial devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dkkeller/detectty.git",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts' : [
            'detectty = detectty.detectty:detect',
        ],
    },
    package_data={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyserial'
    ],
    python_requires='>=3.6',
)
