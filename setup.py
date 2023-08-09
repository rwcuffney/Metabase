from setuptools import setup, find_packages

VERSION = '3.0.3'

setup(
    name="lexisnexisapi",
    version= VERSION,
    license='MIT',
    author="Robert Cuffney",
    author_email='robert.cuffney@lexisnexis.com',
    description = 'a module to support the lexisnexis metabase search api',
    long_description = ' module provides a Python interface to interact with the Metabase API. It allows you to perform searches and retrieve articles using the Metabase API. The module facilitates the creation of Python objects representing the API response, making it easy to work with the data.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    url='',
    keywords='example project',
    install_requires=[],
     

)
