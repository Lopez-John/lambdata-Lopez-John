"""lambdata_Lopez_John - A collection of Data Science functions"""
import setuptools # available in a standard library

REQUIRED =[
    'numpy',
    'pandas'
]

with open('README.md', 'r') as fh:
        LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name = 'lambdata_Lopez_John',
    version='0.0.2',
    author='Lopez-John',
    description=LONG_DESCRIPTION,
    long_description_contents='text/markdown',
    url="https://github.com/Lopez-John/lambdata-Lopez-John.git",
    #how we want to find out REQUIRED packages
    packages=setuptools.find_packages(), 
    python_requires='>=3.6', #what versions of python we are compatible with
    install_requires =  REQUIRED,
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI approved :: MIT License'
    ]
)