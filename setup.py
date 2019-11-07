# setup.py
# Copyright (C) 2019 Fracpete (fracpete at waikato dot ac dot nz)

from setuptools import setup


setup(
    name="ufdl-python-client",
    description="Core Python library for accessing the UFDL backend, managing the communication.",
    url="https://github.com/waikato-ufdl/ufdl-python-client",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
    ],
    license='Apache License Version 2.0',
    package_dir={
        '': 'src'
    },
    packages=["ufdl_pythonclient"],
    version="0.0.1",
    author='Corey Sterling',
    author_email='coreytsterling@gmail.com',
    install_requires=[
        "requests"
    ]
)
