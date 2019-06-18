# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

requires = [
    'docopt',
]

test_require = [
    'pytest'
]

setup(
    name='kodi-cli',
    version='0.1.0',
    description='Command-line interface for the Kodi media centre',
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    author=u'Thiago Figueiró',
    author_email='thiagocsf@gmail.com',
    url='https://github.com/thiagofigueiro/kodi-cli',
    packages=['kodicli'],
    package_data={
        'kodicli': ['kodicli/'],
    },
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requires,
    tests_require=test_require,
    entry_points={
        'console_scripts': ['kodi=kodicli.cli:main'],
    },
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ),
)
