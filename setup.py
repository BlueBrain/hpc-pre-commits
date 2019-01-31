# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='hpc-pre-commits',
    version='0.1',
    description='Hooks for pre-commit used by HPC team of Blue Brain Project',
    url="https://github.com/BlueBrain/hpc-pre-commits",
    author='HPC Team',
    author_email='hpc-ou-hpc@groupes.epfl.ch',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'pyyaml',
        'six',
    ],
    entry_points=dict(
        console_scripts=[
            'hpc-pc-cmake-build = hpc_pre_commits.cmake_build:main',
        ],
    )
)
