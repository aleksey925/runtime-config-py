# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='runtime-config-py',
    version='0.0.1',
    description='Library for runtime updating project settings.',
    python_requires='<3.11,>=3.8',
    project_urls={"repository": "https://github.com/aleksey925/runtime-config-py"},
    author='Aleksey Petrunnik',
    author_email='petrunnik.a@mail.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
    ],
    packages=[
        'runtime_config',
        'runtime_config.entities',
        'runtime_config.enums',
        'runtime_config.libs',
        'runtime_config.sources',
    ],
    package_dir={"": "src"},
    package_data={},
    install_requires=['aiohttp[speedups]==3.*,>=3.8.1', 'pydantic==1.*,>=1.10.1'],
    extras_require={
        "dev": [
            "autopep8==1.*,>=1.6.0",
            "black==22.*,>=22.8.0",
            "dephell==0.8.3",
            "docutils==0.18.1",
            "flake8==4.*,>=4.0.1",
            "isort==5.*,>=5.10.1",
            "mistune==0.8.4",
            "mypy==0.971",
            "pre-commit==2.*,>=2.19.0",
            "pytest==7.*,>=7.1.2",
            "pytest-asyncio==0.*,>=0.18.3",
            "pytest-cov==3.*,>=3.0.0",
            "pytest-mock==3.*,>=3.8.2",
            "tomlkit==0.7.0",
        ]
    },
)
