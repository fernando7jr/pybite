from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'pybite',
    packages = [
        'pybite',
    ],
    version = '1.0.1',
    description = 'Chunk by chunk iteration made easier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'metadeta96',
    author_email = 'metadeta96@gmail.com',
    url = 'https://github.com/metadeta96/pybite',
    download_url = 'https://github.com/metadeta96/pybite',
    keywords = [
        'iteration', 
        'iter', 
        'iterable', 
        'sequence', 
        'list',
        'tuple',
        'dict',
        'array',
        'chunk',
        'block',
        'processing',
        'data'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.5',
)