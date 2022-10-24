from setuptools import setup, find_packages
from zoolkit import verson
setup(
    name="zoolkit",
    version=verson,
    description="Zoolkit is a CLI tool to help you build your discord bot",
    author="Pranoy Majumdar",
    author_email="officialpranoy@gmail.com",
    packages=find_packages(),
    install_requires=['click', 'rich'],
    entry_points='''
    [console_scripts]
    zoolkit=zoolkit.cli:cli
    '''
)